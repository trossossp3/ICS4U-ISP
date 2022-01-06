import json
import numpy as np
import keras
import keras.preprocessing.text as kpt
from keras.preprocessing.text import Tokenizer
from keras.models import model_from_json

# we're still going to use a Tokenizer here, but we don't need to fit it
tokenizer = Tokenizer(num_words=750)
# for human-friendly printing
labels = ['negative', 'positive']

# read in our saved dictionary
with open('dic.json', 'r') as dictionary_file:
    dictionary = json.load(dictionary_file)

# this utility makes sure that all the words in your input
# are registered in the dictionary
# before trying to turn them into a matrix.


def convert_text_to_index_array(text):
    words = kpt.text_to_word_sequence(text)
    wordIndices = []
    for word in words:
        if word in dictionary:
            wordIndices.append(dictionary[word])
        else:
            print("'%s' not in training corpus; ignoring." % (word))
    return wordIndices


# read in your saved model structure
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
# and create a model from that
model = model_from_json(loaded_model_json)
# and weight your nodes with your saved values
model.load_weights('model.h5')

# okay here's the interactive part

# n1 = 0
# a1 = []
# while 1:

#     # evalSentence = input('Input a sentence to be evaluated, or Enter to quit: ')
#     f = open('test.txt', 'r')
#     evalSentence = f.readline()
#     test = evalSentence

#     if len(evalSentence) == 0:
#         break

#     # format your input for the neural net
#     testArr = convert_text_to_index_array(test)
#     input = tokenizer.sequences_to_matrix([testArr], mode='binary')
#     # predict which bucket your input belongs in
#     if (input.ndim == 1):
#         input = np.array([input])
#     pred = model.predict(input)
#     # and print it for the humons
#     print("%s sentiment; %f%% confidence" %
#           (labels[np.argmax(pred)], pred[0][np.argmax(pred)] * 100))
#     del evalSentence
#     f.close()

while True:

    f = open('input.txt', 'r+')
    line = f.readline()
    f.close()
    if(line[:2] != "**" and line!=''):
        # format your input for the neural net
        testArr = convert_text_to_index_array(line)
        input = tokenizer.sequences_to_matrix([testArr], mode='binary')
           # predict which bucket your input belongs in
        if (input.ndim == 1):
            input = np.array([input])
        pred = model.predict(input)
        # and print it for the humons
        f = open("input.txt",'w+')
        dog =("***"+"%s sentiment; %f%% confidence" %
            (labels[np.argmax(pred)], pred[0][np.argmax(pred)] * 100))
        f.write(dog)
        f.close()
