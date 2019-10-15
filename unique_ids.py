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
  return list(ids.keys())

def find_unique_filenames():
  result = list(db.documents.find())
  filenames = {}
  for i in range(len(result)):
    filename = result[i]['filename'].encode('utf-8')
    try:
      x = filenames[filename]
    except:
      filenames[filename] = ''
  return list(filenames.keys())