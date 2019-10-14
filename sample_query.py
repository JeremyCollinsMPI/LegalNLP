import requests
import os

stanford_ip = os.environ["stanford_ip"]

url='http://172.17.0.3:9000/?properties={"annotators":"parse","outputFormat":"json"}'

sentence = 'I am a moose'

response = requests.post(url, sentence)

print(response.json())