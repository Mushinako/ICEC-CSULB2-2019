#!/usr/bin/env python3
from math import sqrt


def congruent_numbers(an, ad, bn, bd):
    # Check area integer
    if (an * bn) % (2 * ad * bd):
        return 'no'
    # Check side
    cn = sqrt((an * bd) ** 2 + (bn * ad) ** 2)
    if int(cn) != cn:
        return 'no'
    return (an * bn) // (2 * ad * bd)


def main():
    while True:
        try:
            a, b = input().split()
        except EOFError:
            return
        else:
            if '/' in a:
                a_num, a_den = [int(x) for x in a.split('/')]
            else:
                a_num = int(a)
                a_den = 1
            if '/' in b:
                b_num, b_den = [int(x) for x in b.split('/')]
            else:
                b_num = int(b)
                b_den = 1
            res = congruent_numbers(a_num, a_den, b_num, b_den)
            print(res)


if __name__ == '__main__':
    main()
