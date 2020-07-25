#!/usr/bin/env python3

from collections import Counter
import urllib.request
from lxml import etree

import numpy as np

from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import cross_val_score
from sklearn import model_selection

alphabet="abcdefghijklmnopqrstuvwxyzäö-"
alphabet_set = set(alphabet)

# Returns a list of Finnish words
def load_finnish():
    finnish_url="https://www.cs.helsinki.fi/u/jttoivon/dap/data/kotus-sanalista_v1/kotus-sanalista_v1.xml"
    filename="src/kotus-sanalista_v1.xml"
    load_from_net=False
    if load_from_net:
        with urllib.request.urlopen(finnish_url) as data:
            lines=[]
            for line in data:
                lines.append(line.decode('utf-8'))
        doc="".join(lines)
    else:
        with open(filename, "rb") as data:
            doc=data.read()
    tree = etree.XML(doc)
    s_elements = tree.xpath('/kotus-sanalista/st/s')
    return list(map(lambda s: s.text, s_elements))

def load_english():
    with open("src/words", encoding="utf-8") as data:
        lines=map(lambda s: s.rstrip(), data.readlines())
    return lines

def get_features(a):
    features = np.zeros((len(a),29))
    for i, word in enumerate(a):
        for j, char in enumerate(alphabet):
            features[i, j] += word.count(char)
    return features

def contains_valid_chars(s):
    return set(s).issubset(alphabet_set)

def get_features_and_labels():

    fin = load_finnish()
    fin = [i.lower() for i in fin]
    fin = [x for x in fin if contains_valid_chars(x)]

    eng = load_english()
    eng = [x for x in eng if x[0].islower()]
    eng = [i.lower() for i in eng]
    eng = [x for x in eng if contains_valid_chars(x)]

    fin_feat = get_features(fin)
    eng_feat = get_features(eng)
    X = np.concatenate((fin_feat, eng_feat))

    y = np.zeros(len(fin)+len(eng))
    y[len(fin):] = 1

    return X, y


def word_classification():
    X, y = get_features_and_labels()
    model = MultinomialNB()
    #scores = cross_val_score(model, X, y, cv=5)
    gen = model_selection.KFold(n_splits=5, shuffle=True, random_state=0)
    scores = cross_val_score(model, X, y, cv=gen)
    return scores


def main():
    #print(get_features(np.array(["palloä-", "keihäs", "Tietokone", "mörkö"])))
    #print(contains_valid_chars("aoisdjhasdjkaskdää-"))
    #print(contains_valid_chars("ajsdmasdkasikd9jkasdk"))
    get_features_and_labels()
    print("Accuracy scores are:", word_classification())

if __name__ == "__main__":
    main()
