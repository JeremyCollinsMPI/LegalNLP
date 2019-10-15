from make_vector import *
from pymongo import MongoClient

client = MongoClient('172.17.0.2')
db=client.legalnlp

def add_vector(filename, array):
  db.vectors.insert_one({'filename': filename.decode('utf-8'), 'array': array})

def update_vector(filename, array):
  db.vectors.update_one({'filename': filename.decode('utf-8')}, {"$set": {'filename': filename.decode('utf-8'), 'array': array}})

db.vectors.drop()
for filename in filenames:
  array = make_vector(filename)
  add_vector(filename, array)
