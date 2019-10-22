#!/usr/bin/env python3
def puzzle(board, moves):
    for r in range(len(board)):
        if len(board[r]) == 4:
            board[r].append(' ')
            row = r
            break
        if ' ' in board[r]:
            row = r
            break
    col = board[row].index(' ')
    for m in moves:
        # UP
        if m == 'A':
            if row == 0:
                return 'This puzzle has no final configuration.'
            board[row][col] = board[row - 1][col]
            board[row - 1][col] = ' '
            row -= 1
            continue
        # DOWN
        if m == 'B':
            if row == 4:
                return 'This puzzle has no final configuration.'
            board[row][col] = board[row + 1][col]
            board[row + 1][col] = ' '
            row += 1
            continue
        # LEFT
        if m == 'L':
            if col == 0:
                return 'This puzzle has no final configuration.'
            board[row][col] = board[row][col - 1]
            board[row][col - 1] = ' '
            col -= 1
            continue
        # RIGHT
        if col == 4:
            return 'This puzzle has no final configuration.'
        board[row][col] = board[row][col + 1]
        board[row][col + 1] = ' '
        col += 1
    return '\n'.join([' '.join(row) for row in board])


def main():
    i = 1
    t = input().strip()
    while t != 'Z':
        board = [list(t)] + [list(input().strip()) for _ in range(4)]
        moves = ''
        m = input().strip()
        while True:
            if m[-1] == '0':
                moves += m[:-1]
                break
            else:
                moves += m
                m = input().strip()
        res = puzzle(board, moves)
        print('Puzzle #{}:'.format(i))
        print(res)
        t = input().strip()
        # if t != 'Z':
        #     i += 1
        #     print()
        i += 1
        print()


if __name__ == '__main__':
    main()
