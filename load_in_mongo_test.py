from load_in_mongo import *

def test1():
  db.documentstest.drop()
  dictionary = {'a':'moose'}
  add_dictionary_test(dictionary)
  dictionary = {'b':'moose'}
  add_dictionary_test(dictionary)
  example = find_one_test()
  assert example['value'] == 'moose'
  
test1()
print('Passed')