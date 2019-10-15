from pymongo import MongoClient
import sys

client = MongoClient('172.17.0.2')
db=client.legalnlp

def search_by_id(id):
  result = db.documents.find({'id': id})
  result = list(result)
  return result

def search_by_id_and_filename(id, filename):
  result = db.documents.find({'id': id, 'filename': filename})
  result = list(result)
  return result

def search_by_id_and_filename_test(id, filename):
  result = db.documentstest.find({'id': id, 'filename': filename})
  result = list(result)
  return result

def search_by_filename(filename):
  result = db.documents.find({'filename': filename})
  result = list(result)
  return result

if __name__ == '__main__':
  id = sys.argv[1]
  print(search_by_id(id))