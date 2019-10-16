#!/usr/bin/env python3
def unique_str(s):
    for i in range(len(s)):
        if i != s.index(s[i]):
            return False
    return True


def latin_squares(n, block):
    all_chars = set()
    # Iterate through rows
    for row in block:
        if not unique_str(row):
            return 'No'
        all_chars |= set(row)
        if len(all_chars) != n:
            return 'No'
    # Iterate through columns
    for col in zip(*block):
        if not unique_str(col):
            return 'No'
    # Check reduced
    row = block[0]
    for i in range(n - 1):
        if row[i] > row[i + 1]:
            return 'Not reduced'
    for i in range(n - 1):
        if block[i][0] > block[i + 1][0]:
            return 'Not reduced'
    return 'Reduced'


def main():
    while True:
        try:
            n = int(input())
        except EOFError:
            return
        else:
            block = [input().strip() for _ in range(n)]
            res = latin_squares(n, block)
            print(res)


if __name__ == '__main__':
    main()
