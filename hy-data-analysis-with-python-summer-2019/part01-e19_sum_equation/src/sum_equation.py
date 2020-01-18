#!/usr/bin/env python3

def sum_equation(L):
    #if empty list
    if len(L) == 0:
        return "0 = 0"
    #if not empty, return equation as string
    return " + ".join([str(x) for x in L]) + f" = {sum(L)}"

def main():
    pass

if __name__ == "__main__":
    main()
