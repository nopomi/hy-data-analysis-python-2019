#!/usr/bin/env python3

import math

def solve_quadratic(a, b, c):
    subsection = math.sqrt(b**2 - 4*a*c)
    positive_root = (-1*b + subsection)/(2*a)
    negative_root = (-1*b + (-1*subsection))/(2*a)
    return (positive_root,negative_root)


def main():
    print(solve_quadratic(1,-3,2))
    print(solve_quadratic(1,2,1))

if __name__ == "__main__":
    main()
