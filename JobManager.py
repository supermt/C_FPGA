import snowflake
import sys
import time

class Job(object):
    id=0
    predicate = None

    def __init__(self, id , predicate):
        self.id = id
        self.predicate = predicate

def generateId():
    return long(int(round(time.time() * 1000)))

def createJob(uniqueId,predicate):
    job = Job(uniqueId,predicate)
    return job
    
def submitJobs(Jobs):
    return 