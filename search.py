from pymongo import MongoClient
import sys
import os
import nltk
from nltk.corpus import wordnet as wn
from unique_words import *

try:
  wn.synsets('dog')
except:
  nltk.download('wordnet') 
  wn.synsets('dog')

mongo_ip = os.environ['mongo_ip']
client = MongoClient(mongo_ip)
db = client.legalnlp

unique_words = find_unique_words()

def search_by_word(word):
  result_list = []
  for i in range(100):
    result = db.documents.find({'tokens.' + str(i): word})
    for member in result:
      result_list.append(member)
  return result_list

def get_hyponyms(word):
  synsets  = wn.synsets(word)
  result = []
  for synset in synsets:
    hyponyms = synset.hyponyms()
    result = result + [x._lemma_names[0] for x in hyponyms]
  return result

def get_hyponyms_synset_recursive(synset):
  result = []
  result = result + synset.hyponyms()
  for member in result:
    result = result + get_hyponyms_synset_recursive(member)
  return result

def get_hyponyms_recursive(word):
  synsets  = wn.synsets(word)
  result = []
  for synset in synsets:
    result = result + get_hyponyms_synset_recursive(synset)
  result = [x._lemma_names[0] for x in result]
  return result

def search_hyponyms(word):
  hyponyms = get_hyponyms(word)
  result = []
  for hyponym in hyponyms:
    to_add = search_by_word(hyponym)
    result = result + to_add
  return result

def search_by_similarity(word):  
  synsets  = wn.synsets(word)
  result = []
  documents = db.documents.find()
  for synset in synsets:
    for unique_word in unique_words:
      unique_word = unique_word.decode('utf-8')
      synsets2 = wn.synsets(unique_word)
      for synset2 in synsets2:
        similarity = synset.path_similarity(synset2)
        try:
         if similarity > 0.4:
           result.append(unique_word)
        except:
           pass
  return result


if __name__ == '__main__':
#   id = sys.argv[1]
  word = 'machine'
  result = search_by_similarity(word)
#   result = get_hyponyms_recursive(word)
#   print(len(result))
  print(result)
#   print(len(result[0]))
  
  
