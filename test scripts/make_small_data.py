import numpy as np
import json
from sklearn.model_selection import train_test_split
import random

def rand_emot():
    e = ["(o_o)",":-)",":P",":D","x)","ᓚᘏᗢ","╯°□°）╯︵ ┻━┻",":)","*<:-)","^_^","(⌐■_■)","¯\_(ツ)_/¯", "(T_T)",":o"]
    return random.choice(e)

def load_files():
    truth_lines = []
    pair_lines = []
    
    #Load truth JSON
    for line in open('../../pan20-authorship-verification-training-small-truth.jsonl'):
        d = json.loads(line.strip())
        truth_lines.append(d)

    #Load actual fanfic.
    print("loading fanfic...",rand_emot())
    for line in open('../../pan20-authorship-verification-training-small.jsonl'):
        d = json.loads(line.strip())
        pair_lines.append(d)

    print("done loading",rand_emot())
    
    return truth_lines, pair_lines

def write_to_files(truth_lines, pair_lines): #Hardcoded files, delete content in them before running script.

    pair_train, pair_test, label_train, label_test = train_test_split(pair_lines, truth_lines, train_size=0.5, test_size=0.15)

    print("writing fanfic...",rand_emot())
    
    with open('../data/modified/test_truth.jsonl', 'w') as file:
        file.write(
            '\n'.join(json.dumps(i) for i in label_test))
    
    with open('../data/modified/train_truth.jsonl', 'w') as file:
        file.write(
            '\n'.join(json.dumps(i) for i in label_train))

    with open('../data/modified/test_pair.jsonl', 'w') as file:
        file.write(
            '\n'.join(json.dumps(i) for i in pair_test))

    with open('../data/modified/train_pair.jsonl', 'w') as file:
        file.write(
            '\n'.join(json.dumps(i) for i in pair_train))

    print("done writing",rand_emot())

truth_lines, pair_lines = load_files()
write_to_files(truth_lines, pair_lines)
