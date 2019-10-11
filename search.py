from pymongo import MongoClient

client = MongoClient('172.17.0.2')
db=client.legalnlp

def search_by_id(id):
  result = db.documents.find_one({'id': id})
  return result
