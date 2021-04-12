import json
import numpy as np
import random

#I think we can learn a lot from reading some of the documents - to see if there are any trends.
#This script prints a fanfic - random by default.

def rand_emot():
    e = ["(o_o)",":-)",":P",":D","x)","ᓚᘏᗢ","╯°□°）╯︵ ┻━┻",":)","*<:-)","^_^","(⌐■_■)","¯\_(ツ)_/¯", "(T_T)",":o"]
    return random.choice(e)

text_pairs = []
labels = []
fandom = []

#Load truth JSON
for line in open('../data/pan20-authorship-verification-training-small-truth.jsonl'):
    d = json.loads(line.strip())
    labels.append(int(d['same']))

#Load actual fanfic.
print("loading fanfic...",rand_emot())
for line in open('../data/pan20-authorship-verification-training-small.jsonl'):
    d = json.loads(line.strip())
    text_pairs.append(d['pair'])
    fandom.append(d['fandoms'])

print("done loading",rand_emot())

def read():
    global text_pairs, fandom, labels

    index = np.random.random_integers(0, len(text_pairs), 1)[0]
    fan = fandom[index]
    label = " NOT"
    if labels[index]>0:
        label = ""

    print("Reading entry number", index)
    print("The first 600 chars of two stories about {} and {}.\nThe author is{} the same.\n".format(fan[0], fan[1], label))
    print(text_pairs[index][0][:600]+'\n')
    print(text_pairs[index][1][:600])

def r():
    read()

read()
