import textrazor


textrazor.api_key='f0da20a99878e28e5c83cc47e7bf6d478ebbbc4f089d6fec098f7bce'
client = textrazor.TextRazor(extractors=["entities", "topics"])

def analyse_document(document):
  response = client.analyze(document)
  dictionary = {}
  for entity in response.entities:
    dictionary[entity.id] = {'relevance_score': entity.relevance_score, 'confidence_score': entity.confidence_score, 'freebase_types': entity.freebase_types}
  return dictionary 
