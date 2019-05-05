#!/usr/bin/env python3

def detect_ranges(L):
    list = sorted(L)
    list_length = len(list)
    ranges = []
    i = 0
    while i < list_length:
        range_low = list[i]
        range_high = list[i]
        for j in list[i:]:
            if j == list[i]+1:
                range_high = j
                i += 1
        if range_low == range_high:
            ranges.append(range_low)
        else:
            ranges.append((range_low, range_high+1))
        i += 1
    return ranges

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()
