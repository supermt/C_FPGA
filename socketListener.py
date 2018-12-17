#!/usr/bin/env python
#-*- coding:utf-8 -*-
import select
import socket
import sys
import Queue
import JobProducer
 
# Create a TCP/IP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(False)

# STATIC PORT & HOST

if len(sys.argv) == 1:
  PORT = 50007
else:
  PORT = int(sys.argv[1])

MAX_RECV = 1024
MAX_SEND = 1024

# Bind the socket to the port
server_address = ('localhost', PORT)
print('starting up on %s port %s \n' % server_address)
server.bind(server_address)
 
# Listen for incoming connections
server.listen(5)
 
# Sockets from which we expect to read , currently only the Server Socket
inputs = [ server ]
 
# Sockets to which we expect to write , a empty but queueing Client Socket List
outputs = [ ]
 
message_queues = {}

while inputs:
 
    # Wait for at least one of the sockets to be ready for processing
    # print( 'Server Port '+str(server_address[1])+' waiting for the next event')
    readable, writable, exceptional = select.select(inputs, outputs, inputs)
    # Handle inputs
    for s in readable:
 
        if s is server:
            # A "readable" server socket is ready to accept a connection
            connection, client_address = s.accept()
            # print('new connection from', client_address)
            connection.setblocking(False)
            inputs.append(connection)
 
            # Give the connection a queue for data we want to send
            message_queues[connection] = Queue.Queue()
        else:
            data = s.recv(MAX_RECV)
            if data:
                # A readable client socket has data
                # print('received "%s" from %s' % (data, s.getpeername()) )
                # calling JobProducer to produce a job
                JobProducer.dataReceiveingLoop(data)
                message_queues[s].put(data)
                # Add output channel for response
                if s not in outputs:
                    outputs.append(s)
            else:
                # Interpret empty result as closed connection
                # print('closing', client_address, 'after reading no data')
                # Stop listening for input on the connection
                if s in outputs:
                    outputs.remove(s)  # Remove closed clients from the server queue
                inputs.remove(s)    # Remove closed clients from the input queue
                s.close()           # turn off the client connections
 
                # Remove message queue
                del message_queues[s]
    # Handle outputs
    for s in writable:
        try:
            next_msg = message_queues[s].get_nowait()
        except Queue.Empty:
            # No messages waiting so stop checking for writability.
            # print('output queue for', s.getpeername(), 'is empty')
            outputs.remove(s)
        else:
            # print( 'sending "%s" to %s' % (next_msg, s.getpeername()))
            s.send(next_msg)
    # Handle "exceptional conditions"
    for s in exceptional:
        # print('handling exceptional condition for', s.getpeername() )
        # Stop listening for input on the connection
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()
 
        # Remove message queue
        del message_queues[s]