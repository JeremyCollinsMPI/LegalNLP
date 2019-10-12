from pymongo import MongoClient

client = MongoClient('172.17.0.2')
db=client.legalnlp

def find_unique_ids():
  result = list(db.documents.find())
  ids = {}
  for i in range(len(result)):
    id = result[i]['id'].encode('utf-8')
    try:
      x = ids[id]
    except:
      ids[id] = ''
  return ids.keys()

