#!/usr/bin/env python3

import re


def file_listing(filename="src/listing.txt"):
    tuples = []
    with open(filename) as f:
        for line in f:
            items = re.findall(r'\S*\s\d\s\S*\s\S*\s*(\d*)\s([A-Za-z]{3})\s*(\d*)\s(\d\d):(\d\d)\s(\S*)', line)
            items_converted = (int(items[0][0]), items[0][1], int(items[0][2]), int(items[0][3]), int(items[0][4]), items[0][5])
            tuples.append(items_converted)
    return tuples

def main():
    file_listing()

if __name__ == "__main__":
    main()
