#!/usr/bin/env python3


def main():
    for i in range(1,11):
        trip = triple(i)
        squa = square(i)
        if squa > trip:
            break
        print('triple({})=={} square({})=={}'.format(i,trip,i,squa))



def triple(number):
    return number*3

def square(number):
    return number**2

if __name__ == "__main__":
    main()
