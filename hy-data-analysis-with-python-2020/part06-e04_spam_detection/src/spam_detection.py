#!/usr/bin/env python3
import gzip
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def read_files(fraction):
    ham_lines = gzip.open("src/ham.txt.gz").readlines()
    ham_len = int(fraction * len(ham_lines))

    spam_lines = gzip.open("src/spam.txt.gz").readlines()
    spam_len = int(fraction * len(spam_lines))

    ham = ham_lines[:ham_len]
    spam = spam_lines[:spam_len]

    return ham, spam

def spam_detection(random_state=0, fraction=1.0):
    ham, spam = read_files(fraction)
    X_rows = ham + spam

    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(X_rows).toarray()

    y = np.zeros(len(X_rows))
    y[len(ham):] = 1

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=random_state, train_size=0.75)
    model = MultinomialNB()
    model.fit(X_train, y_train)
    y_fitted = model.predict(X_test)

    score = accuracy_score(y_test, y_fitted)
    misclassified = np.sum(y_test != y_fitted)
    
    return score, len(X_test), misclassified

def main():
    accuracy, total, misclassified = spam_detection()
    print("Accuracy score:", accuracy)
    print(f"{misclassified} messages miclassified out of {total}")

if __name__ == "__main__":
    main()
