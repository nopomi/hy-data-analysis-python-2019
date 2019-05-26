#!/usr/bin/env python3

def reverse_dictionary(d):
    reversed = {}
    for key in d.keys():
        for fin in d[key]:
            if fin in reversed.keys():
                reversed[fin].append(key)
            else:
                reversed[fin] = [key]
    return reversed

def main():
    d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    print(reverse_dictionary(d))

if __name__ == "__main__":
    main()
