import json

# different supporting files
TYPE_TEXTFILE = "Text File"
TYPE_RCFILE = "Result Column file"
TYPE_OTHER = "Other Type of File"

# Error messages

MSG_UNSUPPORT_TYPE = -1

# Define the Mock data input

TYPE_INTEGER = 1
TYPE_STRING = 2

# compare symbol

SYMBOL_EQUAL = '='
SYMBOL_MORE = '>'
SYMBOL_MORE_EQUAL = '>='
SYMBOL_LESS = '<'
SYMBOL_LESS_EQUAL = '<='
SYMBOL_NOT_EQUAL = '!='

class SourceData:
  """ The Modeling Class of Source Data transport from the HDFS cluster"""
  conditions = []
  filepath = ""
  filetype = TYPE_TEXTFILE
  expression = ""

def compileFromJson(sourceString):
  targetData = SourceData()
  stringObject = json.loads(sourceString)
  targetData.conditions = stringObject['conditions']
  targetData.filepath = stringObject['filepath']
  targetData.expression = stringObject['expression']
  targetData.filetype = stringObject['filetype']
  return targetData

class Condition:
  columnIndex = 0
  symbol = SYMBOL_EQUAL
  type = TYPE_INTEGER
  # when ever the value has been load , this value will only be considered as a string type value
  # only when these data has been set to C program and FPGA process block , they will be transfer to
  # integer value
  value = ""

  def __init__(self,targetObject):
    # targetObject = json.loads(jsonString)
    self.columnIndex = targetObject["columnIndex"]
    self.symbol = targetObject["symbol"]
    self.type = targetObject["type"]
    self.value = str(targetObject["value"])


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
