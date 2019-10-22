#!/usr/bin/env python3
def score(s):
    tot = 0
    i = 1
    for c in s:
        if c == 'O':
            tot += i
            i += 1
        else:
            i = 1
    return tot


def main():
    t = int(input())
    for _ in range(t):
        s = input()
        res = score(s)
        print(res)


if __name__ == '__main__':
    main()
