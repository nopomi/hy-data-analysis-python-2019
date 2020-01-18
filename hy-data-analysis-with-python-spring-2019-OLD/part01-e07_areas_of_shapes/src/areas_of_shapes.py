#!/usr/bin/env python3

import math

def main():
    while(True):
        shape = input('Choose a shape (triangle, rectangle, circle): ')
        if shape == 'triangle':
            base = int(input('Give base of the triangle: '))
            height = int(input('Give height of the triangle: '))
            print('The area is %f' % (base*height/2))
        elif shape == 'rectangle':
            width = int(input('Give width of the rectangle: '))
            height = int(input('Give height of the rectangle: '))
            print('The area is %f' % (width*height))
        elif shape == 'circle':
            radius = int(input('Give radius of the circle: '))
            print('The area is %f' % (math.pi*radius**2))
        elif shape == '':
            break
        else:
            print('Unknown shape!')
            continue

if __name__ == "__main__":
    main()
