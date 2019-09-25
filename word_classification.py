import tensorflow as tf
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.models import Model
import numpy as np

inputs = np.load('train_inputs.npy')
labels = np.load('train_labels.npy')

input_shape = np.shape(inputs)

inputs = np.reshape(inputs, (input_shape[0], input_shape[1] * input_shape[2]))

  
input_layer = Input(shape=(input_shape[1] * input_shape[2]))

predictions = Dense(1, activation='sigmoid')(input_layer)

model = Model(inputs=input_layer, outputs=predictions)
model.compile(optimizer='rmsprop',
              loss='mean_squared_error',
              metrics=['accuracy'])

model.fit(inputs, labels, epochs=10)  # starts training

test_inputs = np.load('test_inputs.npy')
test_labels = np.load('test_labels.npy')
test_input_shape = np.shape(test_inputs)

try:
  test_inputs = np.reshape(test_inputs, (test_input_shape[0], test_input_shape[1] * test_input_shape[2]))
except:
  pass

predictions = model.predict(test_inputs)
print(predictions)
print(test_labels)