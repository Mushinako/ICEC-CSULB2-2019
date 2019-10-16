#!/usr/bin/env python3
def unique_str(s):
    for i in range(len(s)):
        if i != s.index(s[i]):
            return False
    return True


def latin_squares(n, block):
    all_chars = set()


def main():
    while True:
        try:
            n = int(input())
        except EOFError:
            return
        else:
            block = [input() for _ in range(n)]
            res = latin_squares(n, block)
            print(res)


if __name__ == '__main__':
    main()
