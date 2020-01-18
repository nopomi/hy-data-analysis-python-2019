#!/usr/bin/env python3
"""This module provides useful tools for math related to right-sided triangles"""
import math

def hypothenuse(a, b):
    """Return the hypothenuse length when given side lengths of a
    right-angled triangle."""
    c_squared = a**2 + b**2
    return math.sqrt(c_squared)

def area(a, b):
    """Return the area of a right-angled triangle when given the side lengths."""
    return (a * b)/2

def main():
    pass

if __name__ == "__main__":
    main()

__version__ = "0.1"
__author__ = "Miska Noponen"
