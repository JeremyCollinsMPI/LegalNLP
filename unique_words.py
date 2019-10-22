from pymongo import MongoClient

client = MongoClient('172.17.0.2')
db=client.legalnlp

def find_unique_words():
  result = list(db.documents.find())
  result = db.documents.find()
  words = {}
  for member in result:
    tokens = member['tokens']
    for token in tokens.values():
      token = token.encode('utf-8')
      try:
        x = words[token] 
      except:
        words[token] = ''
  return list(words.keys())
  
