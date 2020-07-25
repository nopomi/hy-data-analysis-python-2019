#!/usr/bin/env python3

import sys

def file_count(filename):
    with open(filename) as f:
        words = 0
        chars = 0
        for lines, line in enumerate(f):
            chars+=len(line)
            for word in line.split():
                words+=1
    return (lines+1, words, chars)

def main():
    for file in sys.argv[1:]:
        lines, words, chars = file_count(file)
        print(f"{lines}\t{words}\t{chars}\t{file}")

if __name__ == "__main__":
    main()
