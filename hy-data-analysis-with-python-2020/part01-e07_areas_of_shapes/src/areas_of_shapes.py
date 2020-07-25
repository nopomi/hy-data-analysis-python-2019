#!/usr/bin/env python3

import math


def main():
    while(True):
        shape = input("Choose a shape (triangle, rectangle, circle): ")
        if shape == 'triangle':
            base = int(input("Give the base of the triangle: "))
            height = int(input("Give the height of the triangle: "))
            print("The area is "+ str(base * height / 2))
        elif shape == 'rectangle':
            width = int(input("Give the width of the triangle: "))
            height = int(input("Give the height of the triangle: "))
            print("The area is "+str(width*height))
        elif shape == 'circle':
            radius = int(input("Give radius of the circle: "))
            print("The area is "+str(math.pi*(radius**2)))
        elif shape == '':
            break;
        else:
            print("Unknown shape!")

if __name__ == "__main__":
    main()
