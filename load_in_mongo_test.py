from load_in_mongo import *

def test1():
  db.documentstest.drop()
  dictionary = {'a':'moose', 'filename': 'a.txt'}
  add_dictionary_test(dictionary)
  dictionary = {'b':'moose', 'filename': 'a.txt'}
  add_dictionary_test(dictionary)
  example = find_one_test()
  assert example['value'] == 'moose'
  assert example['filename'] == 'a.txt'
  
test1()
print('Passed')