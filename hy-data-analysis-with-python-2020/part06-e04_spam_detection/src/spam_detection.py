#!/usr/bin/env python3
import gzip
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB


def read_files(fraction):
    ham_lines = int(len(gzip.open("src/spam.txt.gz").readlines()) * fraction)
    spam_lines = int(len(gzip.open("src/spam.txt.gz").readlines()) * fraction)

    ham = np.array(ham_lines)
    with gzip.open("src/ham.txt.gz") as f:
        for i, line in enumerate(f):
            if i > ham_lines: break
            if line == "": continue
            ham = np.append(ham,line)

    spam = np.array(spam_lines)
    with gzip.open("src/spam.txt.gz") as f:
        for i, line in enumerate(f):
            if i > spam_lines: break
            if line== "": continue
            spam = np.append(spam, line)

    return ham, spam

def spam_detection(random_state=0, fraction=1.0):
    ham, spam = read_files(fraction)
    vectorizer = CountVectorizer()
    X_ham = vectorizer.fit_transform(ham)
    X_spam = vectorizer.fit_transform(spam)
    print(X_ham.dtype)
    return 0.0, 0, 0

def main():
    accuracy, total, misclassified = spam_detection()
    print("Accuracy score:", accuracy)
    print(f"{misclassified} messages miclassified out of {total}")

if __name__ == "__main__":
    main()
