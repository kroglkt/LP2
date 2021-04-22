import argparse
import json
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer

#Just ripped form Manex' script in order to understand the data.
#Forget about argparse for now - hardcoded path it is.

#Only train on 100 texts for now - too slow otherwise.
subset = 100

#No clue why it is called gold.
gold = {}

#Load truth JSON
for line in open('data/pan20-authorship-verification-training-small-truth.jsonl'):
    d = json.loads(line.strip())
    gold[d['id']] = int(d['same'])

labels = []
text_pairs = []

#Load actual fanfic.
print("loading fanfic... (•_•)")
for line in open('data/pan20-authorship-verification-training-small.jsonl'):
    d = json.loads(line.strip())
    if d['id'] in gold:
        text_pairs.append(d['pair'])
        labels.append(gold[d['id']])

print("done loading *<:-)")

#Split into train/test data, 20% test
train_text_x, test_text_x, train_y, test_y = train_test_split(text_pairs[:subset], labels[:subset], test_size=0.2)

#Not sure why we want to fit the vectorizer to joined text? Perhaps that is just the way to do it.
text_pairs_joined = [text1 + " " + text2 for text1,text2 in train_text_x]
vectorizer = CountVectorizer()
vectorizer.fit(text_pairs_joined)

vector_pairs = []

#Vectorize each document.
for pair in train_text_x:
    vector_pairs = vectorizer.transform(pair)

print(vector_pairs[0])

#https://direct.mit.edu/coli/article/41/3/481/1519/Computational-Constancy-Measures-of-Texts-Yule-s-K

