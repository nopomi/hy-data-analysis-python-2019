#!/usr/bin/env python3

def extract_numbers(s):
    inputs = s.split()
    L = []
    for item in inputs:
        try:
            L.append(int(item))
        except ValueError:
            print("Not an int")
            try:
                L.append(float(item))
            except ValueError:
                print("Not a float either")
    return L

def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()
