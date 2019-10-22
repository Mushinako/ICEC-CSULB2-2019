#!/usr/bin/env python3
def squares(n, lines):
    counters = []
    for s in range(1, n):
        count = 0
        bound = n - s
        for x in range(1, bound + 1):
            for y in range(1, bound + 1):
                success = True
                for i in range(s):
                    subset = set()
                    subset.add('H {1} {0}'.format(x + i, y))
                    subset.add('V {0} {1}'.format(x + s, y + i))
                    subset.add('H {1} {0}'.format(x + s - i - 1, y + s))
                    subset.add('V {0} {1}'.format(x, y + s - i - 1))
                    if not subset < lines:
                        success = False
                        break
                if success:
                    count += 1
        counters.append(count)
    times = ['{0} square (s) of size {1}'.format(counters[i], i+1)
             for i in range(len(counters)) if counters[i] != 0]
    if not times:
        return 'No completed squares can be found.'
    return '\n'.join(times)


def main():
    i = 1
    while True:
        try:
            n = int(input())
            # if not n:
            #     return
            if i != 1:
                print()
                print('*' * 34)
                print()
        except EOFError:
            return
        m = int(input())
        lines = set([input() for _ in range(m)])
        res = squares(n, lines)
        print('Problem #{}'.format(i))
        print()
        print(res)
        i += 1


if __name__ == '__main__':
    main()
