from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from nltk.stem.snowball import SnowballStemmer
from sklearn.metrics import accuracy_score
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import speech_recognition as sr
import pandas as pd
import pyaudio
import pickle
import time
import nltk
import re

data = pd.read_csv('output.csv')

print(data.shape)

for i in range(data.shape[0]):
    print(data["Вопрос"][i],data["Ответ"][i])
    print('')
    time.sleep(1)
