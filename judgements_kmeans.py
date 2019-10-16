from kmeans_analysis import *
import os
from pymongo import MongoClient
import sys
import numpy as np
from unique_ids import *

def find_indices(my_list, whatever):
  indices = [i for i, x in enumerate(my_list) if x == whatever]
  return indices

mongo_ip = os.environ['mongo_ip']
client = MongoClient(mongo_ip)
db=client.legalnlp

vector_list = db.vectors.find()
array = []
for thing in vector_list:
  vector = thing['array']
  array.append(vector)
array = np.array(array)

ids = find_unique_ids()

kmeans = kmeans_analysis(array)

predictions = kmeans.predict(array)

j = 0
while j < 21:
  
  indices = find_indices(predictions, j)
  
  vectors = []
  for member in indices:
    vectors.append(array[member])

  vectors = np.array(vectors)
  length = vectors.shape[1]
  for i in range(length):
    mean = np.mean(np.take(vectors, i, 1))
    median = np.median(np.take(vectors, i, 1))
    if median > 0.9:
      print(ids[i])
  print(len(indices))
  j = j + 1
  inputm = input()
