from selenium import webdriver
import html2text
import os

browser = webdriver.Chrome()

DIS = 1

output_directory = 'texts'

if not os.path.exists(output_directory):
  os.mkdir(output_directory)

while DIS < 10:

  browser.get('https://legalref.judiciary.hk/lrs/common/ju/ju_body.jsp?DIS=' + str(DIS) + '&AH=&QS=&FN=&currpage=#')
  html = browser.page_source
  text = html2text.html2text(html)
  text = text.encode('utf-8')
  file = open(output_directory + '/' + str(DIS) + '.txt', 'w')
  file.write(text)
  DIS = DIS + 1

browser.close()