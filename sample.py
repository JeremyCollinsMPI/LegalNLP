from submit_file import *

bc = connect_to_server('192.168.1.57')
file = open('sample.txt','r').readlines()
encodings = submit_file(file, bc)
print(encodings)