#!/usr/bin/env python3

import pandas as pd

def read_series():
    indices = []
    values = []
    while True:
        text = input("Give value and index: ")
        if not text:
            break
        try:
            index, value = text.split()
        except ValueError:
            print('The input was malformed')
            continue
        indices.append(index)
        values.append(value)
    return pd.Series(values, index=indices)

def main():
    print(read_series())

if __name__ == "__main__":
    main()
