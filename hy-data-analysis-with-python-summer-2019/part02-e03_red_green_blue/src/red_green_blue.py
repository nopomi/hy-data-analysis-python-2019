#!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):
    colors = []
    with open(filename, "r") as f:
        next(f) #disregard first line
        for line in f:
            m = re.match(r'\s*(\d+)\s+(\d+)\s+(\d+)\s+(.*)', line)
            colors.append(f"{m.group(1)}\t{m.group(2)}\t{m.group(3)}\t{m.group(4)}")
    return colors


def main():
    print(red_green_blue())

if __name__ == "__main__":
    main()
