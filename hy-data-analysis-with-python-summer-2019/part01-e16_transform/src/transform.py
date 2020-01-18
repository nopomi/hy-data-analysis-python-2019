#!/usr/bin/env python3

def transform(s1, s2):
    #convert to list of integers
    s1_int = map(int, s1.split())
    s2_int = map(int, s2.split())
    #multiplicate elements and add to one list
    zipped = zip(s1_int, s2_int)
    L = []
    for i in zipped:
        L.append(i[0]*i[1])
    return L

def main():
    print(transform("1 5 3", "2 6 -1"))

if __name__ == "__main__":
    main()
