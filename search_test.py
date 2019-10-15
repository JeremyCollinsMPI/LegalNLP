from search import *

def test1():
  id = 'b'
  filename = 'a.txt'
  result = search_by_id_and_filename_test(id, filename)
  assert len(result) == 1

test1()
print('Passed')