import requests
import os

stanford_ip = os.environ["stanford_ip"]
url = 'http://' + stanford_ip + ':9000/?properties={"annotators":"parse","outputFormat":"json"}'

def segment_file(filename):
  file = open(filename, 'r', encoding = 'utf-8').read()
  response = requests.post(url, file.encode('utf-8'))
  dict = response.json()
  return dict
  
def find_tokens(dict):
  token_sets = []
  for i in range(len(dict['sentences'])):
    tokens = dict['sentences'][i]['tokens']
    tokens = [x['originalText'] for x in tokens]
    token_sets.append(tokens)
  return token_sets

def token_set_to_sentence(token_set):
  return ' '.join(token_set)


