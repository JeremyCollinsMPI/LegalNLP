import requests
import html2text
import os


DIS = 1

output_directory = 'texts'

if not os.path.exists(output_directory):
  os.mkdir(output_directory)

while DIS < 20000:
  try:
    response = requests.get('https://legalref.judiciary.hk/lrs/common/ju/ju_body.jsp?DIS=' + str(DIS) + '&AH=&QS=&FN=&currpage=#')
    html = response.text
    text = html2text.html2text(html)
    text = text.encode('utf-8')
    if 'Sorry, the page you requested cannot be found.' in text:
      pass
    else:
      file = open(output_directory + '/' + str(DIS) + '.txt', 'w')
      file.write(text)
  except:
    pass
  DIS = DIS + 1

