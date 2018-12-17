import json
import dataFormate
import FileReader
import JobManager

def dataReceiveingLoop(sourceString):
  # print 'Into Receiveing Process Loop'
  decodeData = dataFormate.compileFromJson(sourceString)
  print decodeData.conditions
  # loading files according to different file type as memory block
  if decodeData.filetype == dataFormate.TYPE_TEXTFILE: 
    targetFile = FileReader.loadTextFile(decodeData.filepath)
  elif decodeData.filetype == dataFormate.TYPE_RCFILE:
    targetFile = FileReader.loadRCFile
  else:
    print "Can not support current file type"
    return
  # validate file and condition list, in case there are something unexpected happen
  if not validate(decodeData.conditions,targetFile):
    print "Error Occurred"
    return

  # reading predicates
  # prepare a list for predicates , each predicates has a memory block and a atom filter
  predicatesList=[]

  for condition in decodeData.conditions:
    predicate = dataFormate.Condition(condition)
    # print("the comparison operator is %s" % predicate.symbol)
    predicatesList.append(predicate)

  
  Jobs = FileReader.loadTEXTTargetColumns(targetFile.fileOperator,predicate)

  JobManager.submitJobs(Jobs)

    # print JobManager.generateId()
    # JobManager.createJob(JobManager.generateId,predicate)


def validate(conditions , targetFile):
  return True

"""
mockdata = {
    "conditions": [
        {
            "columnIndex": 0,
            "symbol": SYMBOL_EQUAL,
            "type": TYPE_INTEGER,
            "value": 1234
        },
        {
            "columnIndex": 4,
            "symbol": SYMBOL_NOT_EQUAL,
            "type": TYPE_STRING,
            "value": "just 6666"
        }
    ],
    "filepath": "/Users/MT/git/C_FPGA/targetpack",
    "filetype": dataFormater.TYPE_TEXTFILE,
    "expression": "A && B || C"
}
"""