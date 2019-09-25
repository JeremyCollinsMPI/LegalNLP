import numpy as np
from submit_file import *
import pandas as pd

def rep(x, y):
  result = []
  for i in range(y):
    result.append(x)
  return result

bc = connect('127.0.0.1')

train_texts = pd.read_csv('train_texts.txt', header=0)
test_texts = pd.read_csv('test_texts.txt', header=0)

train_inputs = bc.encode(train_texts.text.tolist())
train_labels = np.array(train_texts.label.tolist())
test_inputs = bc.encode(test_texts.text.tolist())
test_labels = np.array(test_texts.label.tolist())
np.save('train_inputs', train_inputs)
np.save('train_labels', train_labels)
np.save('test_inputs', test_inputs)
np.save('test_labels', test_labels)


