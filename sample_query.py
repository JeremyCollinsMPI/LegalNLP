import requests
import os

stanford_ip = os.environ["stanford_ip"]

url='http://172.17.0.3:9000/?properties={"annotators":"parse","outputFormat":"json"}'

# sentence = 'I am a moose.  You are a dog'
sentence = open('judgements/texts/1.txt')

response = requests.post(url, sentence)


dict = response.json()
print(len(dict['sentences']))
print(dict['sentences'][20])