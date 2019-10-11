from load_in_mongo import *
from textrazor_analysis import *
from search import *

filename = 'result.txt'
dictionary = analyse_document(filename)
add_dictionary(dictionary)
print(search_by_id('Lawsuit'))

