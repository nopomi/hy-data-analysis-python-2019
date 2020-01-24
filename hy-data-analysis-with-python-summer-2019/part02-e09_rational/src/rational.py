#!/usr/bin/env python3

class Rational(object):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, number):
        num = (self.a*number.b) + (self.b*number.a)
        denom = self.b*number.b
        return Rational(num, denom)

    def __sub__(self, number):
        num = (self.a*number.b) - (self.b*number.a)
        denom = self.b*number.b
        return Rational(num, denom)

    def __truediv__(self, number):
        return Rational(self.a*number.b,self.b*number.a)

    def __mul__(self, number):
        return Rational(self.a*number.a, self.b*number.b)

    def __eq__(self, number):
        return (self.a/self.b) == (number.a/number.b)

    def __gt__(self, number):
        return (self.a/self.b) > (number.a/number.b)

    def __lt__(self, number):
        return (self.a/self.b) < (number.a/number.b)

    def __str__(self):
        return f"{self.a}/{self.b}"


def main():
    r1=Rational(1,4)
    r2=Rational(2,3)
    print(r1)
    print(r2)
    print(r1*r2)
    print(r1/r2)
    print(r1+r2)
    print(r1-r2)
    print(Rational(1,2) == Rational(2,4))
    print(Rational(1,2) > Rational(2,4))
    print(Rational(1,2) < Rational(2,4))

if __name__ == "__main__":
    main()
