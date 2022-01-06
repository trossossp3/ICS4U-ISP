import numpy as np
import json
import keras
import keras.preprocessing.text as kpt
from keras.preprocessing.text import Tokenizer

from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation

#find most popular words and use those
max_words = 750

tokenizer = Tokenizer(num_words=max_words)


#extract data from csv
#only use cols 1,3
training = np.genfromtxt('data.csv', delimiter=',', skip_header=1, usecols=(
    1, 3), dtype=None, encoding=None)

train_x = [x[1] for x in training]
# index all the sentiment labels
train_y = np.asarray([x[0] for x in training])

#sort data into dictionary with most frequent words having lower index
tokenizer.fit_on_texts(train_x)

#tokenizer comes with its own dictionary of words with IDs

dictionary = tokenizer.word_index
#save it to json
with open('dic.json','w') as dictionary_file:
    json.dump(dictionary,dictionary_file)

def convert_text_to_index_array(text):
    
    return [dictionary[word] for word in kpt.text_to_word_sequence(text)]

allWordIndices = []
# for each tweet, change each token to its ID in the Tokenizer's word_index
for text in train_x:
    wordIndices = convert_text_to_index_array(text)
    allWordIndices.append(wordIndices)

# now we have a list of all tweets converted to index arrays.
# cast as an array for future usage.
allWordIndices = np.asarray(allWordIndices)

# create one-hot matrices out of the indexed tweets
train_x = tokenizer.sequences_to_matrix(allWordIndices, mode='binary')
# treat the labels as categories
train_y = keras.utils.to_categorical(train_y, 2)


model = Sequential()
model.add(Dense(512, input_shape=(max_words,), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(256, activation='sigmoid'))
model.add(Dropout(0.5))
model.add(Dense(2, activation='softmax'))

model.compile(loss='categorical_crossentropy',
  optimizer='adam',
  metrics=['accuracy'])

model.fit(train_x, train_y,
  batch_size=32,
  epochs=5,
  verbose=1,
  validation_split=0.1,
  shuffle=True)

model_json = model.to_json()
with open('model.json', 'w') as json_file:
    json_file.write(model_json)

model.save_weights('model.h5')

print('saved model!')
