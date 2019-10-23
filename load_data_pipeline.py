import sys
from get_text import *
from divide_into_sentences import *
from pymongo import MongoClient
import os

mongo_ip = os.environ['mongo_ip']
client = MongoClient(mongo_ip)
db=client.legalnlp

def analyse_segmented(segmented, filename):
  token_sets = find_tokens(segmented)
  for token_set in token_sets:
    dictionary = {}
    dictionary['text'] = token_set_to_sentence(token_set)
    dictionary['filename'] = directory_name.strip('/') + '/' +filename
    dictionary['tokens'] = {}
    j = 0
    for token in token_set:
      dictionary['tokens'][str(j)] = token
      j = j + 1
    db.documents.insert_one(dictionary)
  
def load(directory_name, limit=10000):
  directory = os.listdir(directory_name)
  for filename in directory:
    if '.docx' in filename:
      text = get_text(directory_name + '/' +filename)
      new_file = open(directory_name + '/' + filename.replace('docx', 'txt'), 'w', encoding='utf-8')
      new_file.write(text)
  directory = os.listdir(directory_name)
  for i in range(1000):
    if i >= len(directory):
      break
    filename = directory[i]
    if '.txt' in filename:
      print(filename)
      file = open(directory_name + '/' + filename, 'r', encoding='utf-8').read()
      if len(file) > limit:
        print(len(file))
        print(len(file)/limit)
        parts = int(len(file) / limit)
        for part in range(parts+1):
          print(part)
          print(parts)
          segmented = segment_file(directory_name + '/' +filename, part=part, limit=limit)
          analyse_segmented(segmented, filename + '_part_' + str(part))
          
      else:
        segmented = segment_file(directory_name + '/' +filename)
        analyse_segmented(segmented, filename)


if __name__ == '__main__':
  directory_name = sys.argv[1]
  load(directory_name)