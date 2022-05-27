from tensorflow.keras.models import load_model
import nltk
from nltk.stem import WordNetLemmatizer
import random
import json
import pickle
import numpy as np

nltk.download('punkt', quiet=True)
nltk.download('wordnet', quiet=True)

words = []
classes = []
intent_methods = {}
model = load_model(f'test_model.h5')
lemmatizer = WordNetLemmatizer()
words = pickle.load(open(f'test_model_words.pkl', 'rb'))
classes = pickle.load(open(f'test_model_classes.pkl', 'rb'))
intents = json.loads(open(f'intents.json').read())
    
def _clean_up_sentence( sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

def _bag_of_words( sentence, words):
    sentence_words = _clean_up_sentence(sentence)
    bag = [0] * len(words)
    for s in sentence_words:
        for i, word in enumerate(words):
            if word == s:
                bag[i] = 1
    return np.array(bag)

def _predict_class( sentence):
    p = _bag_of_words(sentence, words)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.1
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    return return_list

def _get_response( ints, intents_json):
    try:
        tag = ints[0]['intent']
        list_of_intents = intents_json['intents']
        for i in list_of_intents:
            if i['tag']  == tag:
                result = random.choice(i['responses'])
                break
    except IndexError:
        result = "I don't understand!"
    return result

def requested( message):
    ints = _predict_class(message)
    if ints[0]['intent'] in intent_methods.keys():
        intent_methods[ints[0]['intent']]()
    else:
        return _get_response(ints, intents)