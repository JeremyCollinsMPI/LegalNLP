import numpy as np
from unique_ids import *
from search import *

def rep(x, y):
  result = []
  for i in range(y):
    result.append(x)
  return result

ids = find_unique_ids()
filenames = find_unique_filenames()

id_dictionary = {}
for i in range(len(ids)):
  id_dictionary[ids[i]] = i

def make_vector(filename):
  array = rep(0, len(ids))
  result = search_by_filename(filename.decode('utf-8'))
  for member in result:
    id = member['id'].encode('utf-8')
    value = len(member['value'])
    id_position = id_dictionary[id]
    array[id_position] = value
  return array




