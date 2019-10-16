#!/usr/bin/env python3
from math import floor, sqrt


def halfway(n):
    k = floor(0.5 + sqrt(0.25 + 0.5 * n * (n - 1)))
    return n - k


def main():
    while True:
        try:
            n = int(input())
        except EOFError:
            return
        else:
            res = halfway(n)
            print(res)


if __name__ == '__main__':
    main()
