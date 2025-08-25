from collections import deque

def wire_DHD_SG1(existing_wires):
    board = []
    start = None
    goal = None
    for line in existing_wires.strip().splitlines():
        board.append(list(line))
        if 'S' in line:
            start = (len(board)-1, line.find('S'))
        if 'G' in line:
            goal = (len(board)-1, line.find('G'))
    if not start or not goal:
        return "Oh for crying out loud..."

    to_process = deque([start])
    finished = False
    last_step = 0
    while 0 < len(to_process):
        row_col = to_process.popleft()
        row = row_col[0]
        col = row_col[1]
        val = board[row][col]
        step = 1
        if isinstance(val, int):
            step = val + 1
        elif val != 'S':
            return "Oh for crying out loud..."

        for i in range(row-1, row+2):
            if not (0 <= i < len(board)):
                continue
            for j in range(col-1, col+2):
                if not (0 <= j < len(board[i])) or (i == row and j == col):
                    continue
                if board[i][j] == 'G':
                    last_step = step - 1
                    finished = True
                elif board[i][j] == '.':
                    board[i][j] = step
                    to_process.append((i, j))

        if finished:
            break

    if not finished:
        return "Oh for crying out loud..."

    found = False
    to_process = deque([goal])
    while 0 < len(to_process):
        row_col = to_process.popleft()
        row = row_col[0]
        col = row_col[1]
        val = board[row][col]
        step = 1
        if isinstance(val, int):
            step = val - 1
        elif val == 'G':
            step = last_step

        neighbours = [(-1,0), (0,-1), (0,1), (1,0), (-1,-1), (-1,1), (1,-1), (1,1)]

        found = False
        for neighbour in neighbours:
            i = row + neighbour[0]
            j = col + neighbour[1]
            if not (0 <= i < len(board)):
                continue
            if not (0 <= j < len(board[i])) or found:
                continue
            if board[i][j] == step or board[i][j] == 'S':
                found = True
                if board[row][col] != 'G':
                    board[row][col] = 'P'
                if board[i][j] == step:
                    to_process.append((i, j))

    res = ""
    for i in range(len(board)):
        for j in range(len(board[i])):
            res += '.' if isinstance(board[i][j], int) else board[i][j]
        res += '\n'
    return res.strip()


if __name__ == '__main__':
    wires = """
.S.
...
.G.
"""
    print(wire_DHD_SG1(wires))
    # should be:
    """
    .S.
    .P.
    .G.
    """
    print()

    wires = """
.S...
XXX..
.X.XX
..X..
G...X
"""
    print(wire_DHD_SG1(wires))
    #should be:
    """
    .SP..
    XXXP.
    .XPXX
    .PX..
    G...X
    """