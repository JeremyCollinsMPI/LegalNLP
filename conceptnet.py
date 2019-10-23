import sys
from get_text import *
from divide_into_sentences import *
from pymongo import MongoClient
import os

mongo_ip = os.environ['mongo_ip']
client = MongoClient(mongo_ip)
db=client.conceptnet

def load_conceptnet_into_mongo(limit = None, write_limit = None, relation_restriction=None):
  with open('conceptnet-assertions-5.7.0.csv',encoding='utf-8') as infile:
    i = 0 
    j = 0
    for line in infile:
      if not limit == None:
        if i > limit:
          break 
      if not write_limit == None:
        if j > write_limit:
          break   
      relation = line.split('\t')[0]
      try:
        relationship = relation.split(',')[0]
        relationship = relationship.split('/')[-2]
        print(relationship)
        if not relation_restriction == None:
          if not relationship == relation_restriction:
            i = i + 1
            print(i)
            continue
        thing1 = relation.split(',')[1]
        thing2 = relation.split(',')[2]
        db.documents.insert_one({'relation': relationship, 'thing1': thing1, 'thing2': thing2})
        print('fine')
      except:
        pass
      i = i + 1
      j = j + 1

def search_conceptnet(dictionary):
  return db.documents.find(dictionary)


# load_conceptnet_into_mongo(20000000, relation_restriction = 'IsA')