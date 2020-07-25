#!/usr/bin/env python3
import string

def word_frequencies(filename):
    frequencies = {}
    with open(filename) as f:
        for line in f:
            for word in line.split():
                word = word.strip(string.punctuation)
                if word in frequencies:
                    frequencies[word] = frequencies[word] + 1
                else:
                    frequencies[word] = 1
    return frequencies

def main():
    print(word_frequencies("src/alice.txt"))

if __name__ == "__main__":
    main()
