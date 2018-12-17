import SourceDataPhrase as dataFormate
import dataFormate

def loadTextFile(filepath):
  targetFile = SourceFile()
  target_file = open(filepath, 'r')
  targetFile.setFileOperator(target_file)
  # reading the headline to define the total schema
  headline = target_file.readline()
  # first divide the string to string lists
  columns = headline.split('\t')
  # then count the columns
  columnCount = len(columns)
  print("file has %d columns" % columnCount)
  targetFile.setTotalColumns(columnCount)
  # Text File is a row based stored engine , counting its total row count 
  # doesn't means something meaningful
  return targetFile

def loadRCFile(filepath):
  return dataFormate.MSG_UNSUPPORT_TYPE

def loadTEXTTargetColumns(fileOperator,predicates,limit=0):
  conditions = []
  for predicate in predicates:
    conditions.append(predicate.)


  return [[],[]]

class FileInfo:
  fileType = dataFormate.TYPE_TEXTFILE
  fileLength = 0
  totalRows = -1
  totalColumns = 0
  fileOperator = None

class SourceFile:
  metaData = FileInfo()
  
  def setFileOperator(self,fileOperator):
    self.metaData.fileOperator = fileOperator

  def setTotalColumns(self,column_counting):
    self.metaData.totalColumns = column_counting