from textrazor_analysis import *
import sys
from get_text import *

from pymongo import MongoClient
import os

mongo_ip = os.environ['mongo_ip']
client = MongoClient(mongo_ip)
db=client.legalnlp

def load(directory_name):
  directory = os.listdir(directory_name)
  for filename in directory:
    if '.docx' in filename:
      text = get_text(directory_name + '/' +filename)
      new_file = open(directory_name + '/' + filename.replace('docx', 'txt'), 'w', encoding='utf-8')
      new_file.write(text)

  directory = os.listdir(directory_name)
  for i in range(0, 5):
    filename = directory[i]
    if '.txt' in filename:
      print(filename)
      dictionary_list = analyse_document(directory_name + '/' +filename)
      for dictionary in dictionary_list:
        db.documents.insert_one(dictionary)

if __name__ == '__main__':
  directory_name = sys.argv[1]
  load(directory_name)
