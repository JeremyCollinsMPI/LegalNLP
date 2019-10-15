from pymongo import MongoClient

client = MongoClient('172.17.0.2')
db=client.legalnlp

def add_dictionary_test(dictionary):
  for key in dictionary.keys():
    if not key == 'filename':
      db.documentstest.insert_one({"id": key, "value": dictionary[key], "filename": dictionary['filename']})

def add_dictionary(dictionary):
  for key in dictionary.keys():
    if not key == 'filename':
      db.documents.insert_one({"id": key, "value": dictionary[key], "filename": dictionary['filename']})

def find_one_test():
  example = db.documentstest.find_one({'id':'a'})
  return example

