LEFT = 3
RIGHT = 1
UP = 4
DOWN = 2

def snail(snail_map):
    top_row = -1
    bottom_row = len(snail_map)
    left_col = -1
    right_col = len(snail_map[0])

    row = 0
    col = 0
    direction = RIGHT
    res = []
    while True:
        if row <= top_row or bottom_row <= row or col <= left_col or right_col <= col:
            break
        res.append(snail_map[row][col])

        if direction == RIGHT:
            if col + 1 == right_col:
                row += 1
                direction = DOWN
                top_row += 1
            else:
                col += 1
        elif direction == DOWN:
            if row + 1 == bottom_row:
                col -= 1
                direction = LEFT
                right_col -= 1
            else:
                row += 1
        elif direction == LEFT:
            if col - 1 == left_col:
                row -= 1
                direction = UP
                bottom_row -= 1
            else:
                col -= 1
        else:
            if row - 1 == top_row:
                col += 1
                direction = RIGHT
                left_col += 1
            else:
                row -= 1
    return res


def next_direction(current_direction):
    return current_direction + 1 if current_direction != UP else RIGHT


if __name__ == '__main__':
    array = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]
    print(snail(array)) #[1,2,3,6,9,8,7,4,5]