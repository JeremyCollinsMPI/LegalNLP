from bert_serving.client import BertClient

def connect_to_server(ip):
  bc = BertClient(ip=ip)
  return bc

def submit_file(file_read_lines, server):
  list = [x.replace('\n','') for x in file_read_lines]
  list = [x for x in list if len(x.replace(' ', '')) > 0]
  return server.encode(list)
  