def get_generation(cells : list[list[int]], generations : int) -> list[list[int]]:
    for _ in range(generations):
        cells = expand_array(cells)
        gen_cells = []
        for row in range(len(cells)):
            gen_cells.append([])
            for col in range(len(cells[row])):
                live = live_neighbours(cells, row, col)
                if cells[row][col] == 1:
                    if 2 <= live <= 3:
                        gen_cells[-1].append(1)
                    else:
                        gen_cells[-1].append(0)
                else:
                    if live == 3:
                        gen_cells[-1].append(1)
                    else:
                        gen_cells[-1].append(0)
        cells = gen_cells

    return shrink_array(cells)


def live_neighbours(cells : list[list[int]], row: int, col: int) -> int:
    live = 0
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            if i == row and j == col:
                continue
            if 0 <= i < len(cells) and 0 <= j < len(cells[i]):
                live += cells[i][j]
    return live


def expand_array(cells : list[list[int]]) -> list[list[int]]:
    expand_left = False
    expand_right = False
    for row in range(len(cells)):
        if cells[row][0] == 1:
            expand_left = True
        if cells[row][-1] == 1:
            expand_right = True

    if expand_left or expand_right:
        for row in range(len(cells)):
            if expand_left:
                cells[row].insert(0, 0)
            if expand_right:
                cells[row].append(0)

    if 1 in cells[0]:
        cells.insert(0, [0 for _ in range(len(cells[0]))])

    if 1 in cells[-1]:
        cells.append([0 for _ in range(len(cells[0]))])

    return cells


def shrink_array(cells : list[list[int]]) -> list[list[int]]:
    while True:
        shrink_left = True
        shrink_right = True
        for row in range(len(cells)):
            if cells[row][0] == 1:
                shrink_left = False
            if cells[row][-1] == 1:
                shrink_right = False

        if shrink_left or shrink_right:
            for row in range(len(cells)):
                if shrink_left:
                    cells[row].pop(0)
                if shrink_right:
                    cells[row].pop(-1)

        shrink_up = 1 not in cells[0]
        if shrink_up:
            cells.pop(0)

        shrink_down = 1 not in cells[-1]
        if shrink_down:
            cells.pop(-1)

        if not shrink_left and not shrink_right and not shrink_up and not shrink_down:
            break

    return cells


if __name__ == '__main__':
    input_arr = [
        [1, 1, 1, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0, 1, 1, 1]
    ]

    print(get_generation(input_arr, 16))

    #result should be:
    """[
        [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1]
    ]"""