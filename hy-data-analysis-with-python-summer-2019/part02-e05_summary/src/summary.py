#!/usr/bin/env python3

import sys
import math

def summary(filename):
    numbers = []
    #get numbers to a list
    with open(filename) as f:
        for number in f:
            try:
                numbers.append(float(number))
            except ValueError:
                print("Not a float")
    #count average
    average = sum(numbers) / len(numbers)
    #count stddev
    diffs = 0
    for i in numbers:
        diffs += (i-average)**2
    stddev = math.sqrt(diffs/(len(numbers)-1))
    return (sum(numbers),average,stddev)

def main():
    for file in sys.argv[1:]:
        sum, avg, stddev = summary(file)
        print(f"File: {file} Sum: {sum:.6f} Average: {avg:.6f} Stddev: {stddev:.6f}")

if __name__ == "__main__":
    main()
