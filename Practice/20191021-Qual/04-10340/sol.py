#!/usr/bin/env python3
def all_in_all(s, t):
    i = j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)


def main():
    while True:
        try:
            s, t = input().split()
        except EOFError:
            return
        else:
            res = all_in_all(s, t)
            print('Yes' if res else 'No')


if __name__ == '__main__':
    main()
