from load_in_mongo import *
from textrazor_analysis import *
import os
import sys
from get_text import *



def load(directory_name):
  directory = os.listdir(directory_name)
  for filename in directory:
    if '.docx' in filename:
      text = get_text(directory_name + '/' +filename)
      new_file = open(directory_name + '/' + filename.replace('docx', 'txt'), 'w', encoding='utf-8')
      new_file.write(text)

  directory = os.listdir(directory_name)
  for filename in directory:
    if '.txt' in filename:
      dictionary = analyse_document(directory_name + '/' +filename)
      add_dictionary(dictionary)

if __name__ == '__main__':
  directory_name = sys.argv[1]
  load(directory_name)
