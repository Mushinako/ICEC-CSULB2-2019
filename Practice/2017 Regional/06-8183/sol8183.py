#!/usr/bin/env python3
def syl(word):
    word = word.lower()
    syl = 0
    return


def haiku(s):
    sent = s.split()


def main():
    while True:
        try:
            s = input().strip()
        except EOFError:
            return
        else:
            res = haiku(s)
            print('\n'.join(res))


if __name__ == '__main__':
    main()
