#!/usr/bin/env python
#-*- coding:utf-8 -*-

import socket
import json
import dataFormate

mockdata = {
    "conditions": [
        {
            "columnIndex": 0,
            "symbol": dataFormate.SYMBOL_EQUAL,
            "type": dataFormate.TYPE_INTEGER,
            "value": 1234
        },
        {
            "columnIndex": 4,
            "symbol": dataFormate.SYMBOL_NOT_EQUAL,
            "type": dataFormate.TYPE_STRING,
            "value": "just 6666"
        }
    ],
    "filepath": "/Users/MT/git/C_FPGA/targetpack",#该部分还有可能给出的是内存地址，则为一个长整形
    "filetype": dataFormate.TYPE_TEXTFILE,
    "expression": "A && B"
}

# Define the sender loops
HOST = '127.0.0.1'    # The remote host
PORT = 50007              # The same port as used by the server
MAX_RECV = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

s.sendall(json.dumps(mockdata))
data = s.recv(10)
print 'Received', repr(data)
s.close()