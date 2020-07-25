#!/usr/bin/env python3

class Prepend(object):

    def __init__(self, s):
        self.start = s

    def write(self, s):
        print(self.start + s)

def main():
    x = Prepend("This first")
    x.write(" - this second")

if __name__ == "__main__":
    main()
