#!/usr/bin/env python3
from math import floor, sqrt


def divisor(n):
    # Ignore 1 and itself
    d = [i for i in range(2, floor(sqrt(n)) + 1) if not n % i]
    all_d = d + [n // x for x in d]
    return sorted(list(set(all_d)))


def star_arrangements(s):
    res = []
    # Find all divisors
    divs = divisor(s)
    res += [(x, x) for x in divs]
    # For all odd divisors, split into 2 lines
    res += [(x // 2 + 1, x // 2) for x in (divs + [s]) if x % 2]
    # For odd number of rows...
    res += [(x + 1, x)
            for x in range(1, s // 3 + 1) if not (s + x) % (2 * x + 1)]
    return sorted(list(set(res)))


def main():
    while True:
        try:
            s = int(input())
        except EOFError:
            return
        except ValueError:
            return
        else:
            res = star_arrangements(s)
            print('{}:'.format(s))
            for x, y in res:
                print(' {0},{1}'.format(x, y))


if __name__ == '__main__':
    main()
