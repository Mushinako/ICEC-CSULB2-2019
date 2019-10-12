#!/usr/bin/env python3
__author__ = 'Lemuel Li, Patrick Feany, and Jonathan Sohrabi'


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        string = ''.join([str(x) for x in range(1, n + 1)])
        res = [0] * 10
        for char in string:
            res[int(char)] += 1
        print(' '.join([str(x) for x in res]))


if __name__ == '__main__':
    main()
