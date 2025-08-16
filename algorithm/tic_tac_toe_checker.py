def is_solved(board):
    columns = [[] for _ in range(len(board[0]))]
    left_diag = []
    right_diag  =[]

    board_filled = True
    for row in range(len(board)):
        if 0 in board[row]:
            board_filled = False
        elif len(set(board[row])) == 1:
            return board[row][0]
        for col in range(len(board[0])):
            columns[col].append(board[row][col])
            if col == row:
                left_diag.append(board[row][col])
                right_diag.append(board[row][-1 - col])

    for column in columns:
        if len(set(column)) == 1 and column[0] != 0:
            return column[0]

    if len(set(left_diag)) == 1 and left_diag[0] != 0:
        return left_diag[0]

    if len(set(right_diag)) == 1 and right_diag[0] != 0:
        return right_diag[0]

    if not board_filled:
        return -1

    return 0


if __name__ == '__main__':
    board = [[0, 0, 1],
             [0, 1, 2],
             [2, 1, 0]]
    print(is_solved(board)) #-1 -> not finished

    board = [[1, 1, 1],
             [0, 2, 2],
             [0, 0, 0]]
    print(is_solved(board))  #1 -> win in row

    board = [[2, 1, 2],
             [2, 1, 1],
             [1, 1, 2]]
    print(is_solved(board))  #1 -> win in column

    board = [[1, 1, 2],
             [2, 1, 1],
             [1, 2, 1]]
    print(is_solved(board))  #1 -> win in diagonal

    board = [[2, 1, 2],
             [2, 1, 1],
             [1, 2, 1]]
    print(is_solved(board))  #0 -> draw