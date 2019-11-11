#!/usr/bin/env python3
def crossword_answers(table, row, col):
    words = []
    # Iterate through the rows
    for r in range(row):
        tr = table[r]
        word = ''
        for c in range(col):
            tc = tr[c]
            if tc == '*':
                if word:
                    words.append(((r, c-len(word)), word, True))
                    word = ''
            else:
                word += tc
        if word:
            words.append(((r, col-len(word)), word, True))
    # Iterate through the cols
    zip_table = list(zip(*table))
    for c in range(col):
        tc = zip_table[c]
        word = ''
        for r in range(row):
            tr = tc[r]
            if tr == '*':
                if word:
                    words.append(((r-len(word), c), word, False))
                    word = ''
            else:
                word += tr
        if word:
            words.append(((row-len(word), c), word, False))
    # I have the list now...
    starts = sorted(set([w[0] for w in words]))
    across = []
    down = []
    for coord, word, acr in sorted(words):
        ind = starts.index(coord)+1
        if acr:
            across.append('%3s' % ind + '.' + word)
        else:
            down.append('%3s' % ind + '.' + word)
    return across, down


def main():
    t = input()
    i = 1
    while True:
        r, c = [int(x) for x in t.split()]
        table = [input() for _ in range(r)]
        across, down = crossword_answers(table, r, c)
        print('puzzle #{}:'.format(i))
        print('Across')
        for acr in across:
            print(acr)
        print('Down')
        for dow in down:
            print(dow)
        t = input()
        if t == '0':
            return
        i += 1
        print()


if __name__ == '__main__':
    main()