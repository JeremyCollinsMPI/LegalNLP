from pymongo import MongoClient
import sys

mongo_ip = os.environ['mongo_ip']
client = MongoClient(mongo_ip)
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