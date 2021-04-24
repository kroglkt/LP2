#import re
#import numpy as np
#import nltk

def get_sent_word_length(text):
    #Function, which removes symbols and count words in sentence
    #Output: length of each sentence & length of each word
    sentences = re.split('[\.+|!|?]', text)
    sentences = [re.sub(r"[^\w]+", ' ', x) for x in sentences if len(x.strip()) != 0]
    word_sentences = [nltk.word_tokenize(x) for x in sentences]
    sentence_lengths = np.array([len(x) for x in word_sentences])
    word_lengths = np.array([len(s) for x in word_sentences for s in x])
    return sentence_lengths, word_lengths

get_sent_word_length(corpus[0])
