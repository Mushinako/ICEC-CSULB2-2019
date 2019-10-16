#!/usr/bin/env python3
__author__ = 'Jonathan Sohrabi, Patrick Feany, and Lemuel Li'


def divisors(n):
    if n == 1:
        return [1]
    if n in (2, 3):
        return [1, n]
    divisors = [1]
    limit = n // 2
    for d in range(2, limit + 1):
        if not n % d:
            divisors.append(d)
    return divisors


def periodic_strings(s):
    length = len(s)
    divs = divisors(length)
    if len(divs) == 1:
        return length
    for d in divs:
        if s[:d] * (length // d) == s:
            return d
    return length


def main():
    t = int(input())
    for i in range(t):
        input()
        s = input().strip()
        res = periodic_strings(s)
        print(res)
        if i == t - 1:
            return
        print()


if __name__ == '__main__':
    main()
