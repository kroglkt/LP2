import json
import numpy as np

#I made this script to create a test JSON file - they did not include one in the PAN dataset for some reason.

test_percent = 0.2

print("Creating train/test files with {}% being test data.".format(test_percent*100))



truth_lines = []
pair_lines = []

#Load truth JSON
for line in open('data/pan20-authorship-verification-training-small-truth.jsonl'):
    d = json.loads(line.strip())
    truth_lines.append(d)

#Load actual fanfic.
print("loading fanfic... (•_•)")
for line in open('data/pan20-authorship-verification-training-small.jsonl'):
    d = json.loads(line.strip())
    pair_lines.append(d)

print("done loading *<:-)")


##### Create JSON files ######

#Make sure, the modified files are empty - otherwise they will just append to them.

test_len = int(len(truth_lines)*test_percent)

print("writing files with {} in test, {} in train".format(test_len, len(truth_lines)-test_len))

#Create test data for truth
with open('data/modified/test_truth.jsonl', 'w') as file:
    file.write(
        '[' +
        ',\n'.join(json.dumps(i) for i in truth_lines[test_len:]) +
        ']\n')

#Create train data for truth
with open('data/modified/train_truth.jsonl', 'w') as file:
    file.write(
        '[' +
        ',\n'.join(json.dumps(i) for i in truth_lines[:test_len]) +
        ']\n')

#Create test data for pairs
with open('data/modified/test_pairs.jsonl', 'w') as file:
    file.write(
        '[' +
        ',\n'.join(json.dumps(i) for i in pair_lines[test_len:]) +
        ']\n')

#Create train data for pairs
with open('data/modified/train_pairs.jsonl', 'w') as file:
    file.write(
        '[' +
        ',\n'.join(json.dumps(i) for i in pair_lines[:test_len]) +
        ']\n')

print("done writing! ^_^")


