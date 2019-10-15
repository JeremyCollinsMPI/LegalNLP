import textrazor

try:
  textrazor.api_key = open('textrazor_api_key.txt', 'r').read()
except:
  print('Put a textrazor api key in a text file named textrazor_api_key.txt.')
  quit()

client = textrazor.TextRazor(extractors=["entities", "topics"])

def clean_up_key(key):
  key = key.replace('.', '[dot]')
  return key

def analyse_document(filename):
  document = open(filename,'r', encoding='utf-8').read()
  dictionary = {}
  response = client.analyze(document)
  for entity in response.entities():
    entity.id = clean_up_key(entity.id)
    entity.id = entity.id.lower()
    try:
      x = dictionary[entity.id]
    except:
      dictionary[entity.id] = []
    dictionary[entity.id].append(entity.matched_text)
  dictionary['filename'] = filename
  print(dictionary['filename'])
  return dictionary 
