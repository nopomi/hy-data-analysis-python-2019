#!/usr/bin/env python3

import math

def solve_quadratic(a, b, c):
    positive_solution = (-1*b + math.sqrt(b**2-4*a*c))/(2*a)
    negative_solution = (-1*b - math.sqrt(b**2-4*a*c))/(2*a)
    return((positive_solution,negative_solution))


def main():
    pass

if __name__ == "__main__":
    main()
