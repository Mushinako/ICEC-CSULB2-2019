#!/usr/bin/env python3
def puzzle(board, moves):
    # Find empty thing
    for r in range(len(board)):
        if ' ' in board[r]:
            row = r
            break
    col = board[row].index(' ')
    # Move
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
        if m == 'R':
            if col == 4:
                return 'This puzzle has no final configuration.'
            board[row][col] = board[row][col + 1]
            board[row][col + 1] = ' '
            col += 1
            continue
    # Return
    return '\n'.join([' '.join(row) for row in board])


def main():
    t = list(input())
    i = 1
    while t[-1] != 'Z':
        board = [t] + [list(input()) for _ in range(4)]
        moves = ''
        while True:
            m = input()
            if m[-1] == '0':
                moves += m[:-1]
                break
            moves += m
        res = puzzle(board, moves)
        print('Puzzle #{}:'.format(i))
        print(res)
        t = list(input())
        if t[-1] != 'Z':
            i += 1
            print()


if __name__ == '__main__':
    main()
