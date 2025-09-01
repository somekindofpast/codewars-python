from enum import Enum

class Direction(Enum):
    RIGHT = 1
    DOWN = 2
    LEFT = 3
    UP = 4

EMPTY_SPACE = '~'

def break_pieces(shape: str):
    grid = []
    row_min_len = 0
    for line in shape.strip('\n').split('\n'):
        grid.append(list(line))
        if row_min_len <= len(grid[-1]):
            row_min_len = len(grid[-1])
        else:
            grid[-1].extend(list(' ' * (row_min_len - len(grid[-1]))))

    top_left_corners = []
    for i in range(len(grid)-1):
        if '+' not in grid[i]:
            continue
        for j in range(len(grid[i])-1):
            if grid[i][j] == '+' and (grid[i+1][j] == '|' or grid[i+1][j] == '+') and (grid[i][j+1] == '-' or grid[i][j+1] == '+'):
                top_left_corners.append((i, j))

    sub_shapes = []
    for tup in top_left_corners:
        sub_shape = [list(EMPTY_SPACE * len(grid[tup[0]])) for _ in range(len(grid))]
        i = tup[0]
        j = tup[1]
        sub_shape[i][j] = '+'
        direction = Direction.RIGHT
        j += 1
        turns = 1
        anti_clockwise_turns = 0
        while not (i == tup[0] and j == tup[1]):
            char = grid[i][j]
            sub_shape[i][j] = char
            match direction:
                case Direction.RIGHT:
                    if char == '+':
                        if i+1 < len(grid) and (grid[i+1][j] == '|' or grid[i+1][j] == '+'):
                            i += 1
                            direction = Direction.DOWN
                            turns += 1
                        elif j+1 < len(grid[i]) and (grid[i][j+1] == '-' or grid[i][j+1] == '+'):
                            sub_shape[i][j] = '-'
                            j += 1
                        else:
                            i -= 1
                            direction = Direction.UP
                            turns += 1
                            anti_clockwise_turns += 1
                    else:
                        j += 1
                case Direction.DOWN:
                    if char == '+':
                        if 0 <= j-1 and (grid[i][j-1] == '-' or grid[i][j-1] == '+'):
                            j -= 1
                            direction = Direction.LEFT
                            turns += 1
                        elif i+1 < len(grid) and (grid[i+1][j] == '|' or grid[i+1][j] == '+'):
                            sub_shape[i][j] = '|'
                            i += 1
                        else:
                            j += 1
                            direction = Direction.RIGHT
                            turns += 1
                            anti_clockwise_turns += 1
                    else:
                        i += 1
                case Direction.LEFT:
                    if char == '+':
                        if 0 <= i-1 and (grid[i-1][j] == '|' or grid[i-1][j] == '+'):
                            i -= 1
                            direction = Direction.UP
                            turns += 1
                        elif 0 < j and (grid[i][j-1] == '-' or grid[i][j-1] == '+'):
                            sub_shape[i][j] = '-'
                            j -= 1
                        else:
                            i += 1
                            direction = Direction.DOWN
                            turns += 1
                            anti_clockwise_turns += 1
                    else:
                        j -= 1
                case Direction.UP:
                    if char == '+':
                        if j+1 < len(grid[i]) and (grid[i][j+1] == '-' or grid[i][j+1] == '+'):
                            j += 1
                            direction = Direction.RIGHT
                            turns += 1
                        elif 0 < i and (grid[i-1][j] == '|' or grid[i-1][j] == '+'):
                            sub_shape[i][j] = '|'
                            i -= 1
                        else:
                            j -= 1
                            direction = Direction.LEFT
                            turns += 1
                            anti_clockwise_turns += 1
                    else:
                        i -= 1

        if anti_clockwise_turns < int(turns / 2) and sub_shape not in sub_shapes:
            sub_shapes.append(sub_shape)

    for index_sub_shape in range(len(sub_shapes)):
        sub_shape = sub_shapes[index_sub_shape]
        for i in range(len(sub_shape)):
            if len(set(sub_shape[i])) == 1:
                continue
            inside_shape = False
            for j in range(len(sub_shape[i])):
                if sub_shape[i][j] == EMPTY_SPACE and 0 <= i - 1:
                    if sub_shape[i - 1][j] == ' ':
                        inside_shape = True
                    elif sub_shape[i - 1][j] == EMPTY_SPACE:
                        inside_shape = False
                if sub_shape[i][j] == '|':
                    inside_shape = not inside_shape
                if inside_shape and sub_shape[i][j] == EMPTY_SPACE:
                    sub_shape[i][j] = grid[i][j]

        while not ('+' in sub_shape[-1]):
            sub_shape.pop(-1)

        while not ('+' in sub_shape[0]):
            sub_shape.pop(0)

        j_min = len(sub_shape[0])
        j_max = 0
        for i in range(len(sub_shape)):
            for j in range(len(sub_shape[i])):
                if sub_shape[i][j] == '+' or sub_shape[i][j] == '|':
                    if j < j_min:
                        j_min = j
                    if j_max < j:
                        j_max = j
                if sub_shape[i][j] == EMPTY_SPACE:
                    sub_shape[i][j] = ' '

        shape_str = ""
        for i in range(len(sub_shape)):
            sub_shape[i] = "".join(sub_shape[i][j_min : j_max+1]).rstrip()
            shape_str += sub_shape[i] + '\n'

        sub_shapes[index_sub_shape] = shape_str.rstrip()


    return sub_shapes

# uncomment next line if you prefer raw error messages
# raw_errors = True


if __name__ == '__main__':
    #shape = '\n+------------+\n|            |\n|            |\n|            |\n+------+-----+\n|      |     |\n|      |     |\n+------+-----+'
    #expected = ['+-----+\n|     |\n|     |\n+-----+', '+------+\n|      |\n|      |\n+------+', '+------------+\n|            |\n|            |\n|            |\n+------------+']

    #shape = '\n+-------------------+--+\n|                   |  |\n|                   |  |\n|  +----------------+  |\n|  |                   |\n|  |                   |\n+--+-------------------+'
    #expected = ['                 +--+\n                 |  |\n                 |  |\n+----------------+  |\n|                   |\n|                   |\n+-------------------+', '+-------------------+\n|                   |\n|                   |\n|  +----------------+\n|  |\n|  |\n+--+']

    #shape = '\n           +-+             \n           | |             \n         +-+-+-+           \n         |     |           \n      +--+-----+--+        \n      |           |        \n   +--+-----------+--+     \n   |                 |     \n   +-----------------+     '
    #expected = ['+-+\n| |\n+-+', '+-----+\n|     |\n+-----+', '+-----------+\n|           |\n+-----------+', '+-----------------+\n|                 |\n+-----------------+']

    #shape = '\n+---+---+---+---+---+---+---+---+\n|   |   |   |   |   |   |   |   |\n+---+---+---+---+---+---+---+---+'
    #expected = ['+---+\n|   |\n+---+', '+---+\n|   |\n+---+', '+---+\n|   |\n+---+', '+---+\n|   |\n+---+', '+---+\n|   |\n+---+', '+---+\n|   |\n+---+', '+---+\n|   |\n+---+', '+---+\n|   |\n+---+']

    #shape = '\n+---+------------+---+\n|   |            |   |\n+---+------------+---+\n|   |            |   |\n|   |            |   |\n|   |            |   |\n|   |            |   |\n+---+------------+---+\n|   |            |   |\n+---+------------+---+'
    #expected = ['+---+\n|   |\n+---+', '+---+\n|   |\n+---+', '+---+\n|   |\n+---+', '+---+\n|   |\n+---+', '+---+\n|   |\n|   |\n|   |\n|   |\n+---+', '+---+\n|   |\n|   |\n|   |\n|   |\n+---+', '+------------+\n|            |\n+------------+', '+------------+\n|            |\n+------------+', '+------------+\n|            |\n|            |\n|            |\n|            |\n+------------+']

    #shape = '\n                 \n   +-----+       \n   |     |       \n   |     |       \n   +-----+-----+ \n         |     | \n         |     | \n         +-----+ '
    #expected = ['+-----+\n|     |\n|     |\n+-----+', '+-----+\n|     |\n|     |\n+-----+']

    #shape = '\n+--------+\n|        |\n|  +--+  |\n|  |  |  |\n|  +--+  |\n|        |\n+--------+'
    #expected = ['+--+\n|  |\n+--+', '+--------+\n|        |\n|  +--+  |\n|  |  |  |\n|  +--+  |\n|        |\n+--------+']

    shape = '\n+-------+ +----------+\n|       | |          |\n| +-+ +-+ +-+    +-+ |\n+-+ | |     |  +-+ +-+\n    | +-----+--+\n+-+ |          +-+ +-+\n| +-+  +----+    | | |\n| |    |    |    +-+ |\n| +----++ +-+        |\n|       | |          |\n+-------+ +----------+'
    expected = ['+-+\n| |\n| |\n| +-----+\n|       |\n+-------+', '+-------+\n|       |\n| +-+ +-+\n+-+ | |\n    | +--------+\n    |          +-+ +-+\n  +-+  +----+    | | |\n  |    |    |    +-+ |\n  +----+  +-+        |\n          |          |\n          +----------+', '+----------+\n|          |\n+-+    +-+ |\n  |  +-+ +-+\n  +--+']

    #shape = '\n         +------------+--+      +--+\n         |            |  |      |  |\n         | +-------+  |  |      |  |\n         | |       |  |  +------+  |\n         | |       |  |            |\n         | |       |  |    +-------+\n         | +-------+  |    |        \n +-------+            |    |        \n |       |            |    +-------+\n |       |            |            |\n +-------+            |            |\n         |            |            |\n    +----+---+--+-----+------------+\n    |    |   |  |     |            |\n    |    |   |  +-----+------------+\n    |    |   |                     |\n    +----+---+---------------------+\n    |    |                         |\n    |    | +----+                  |\n+---+    | |    |     +------------+\n|        | |    |     |             \n+--------+-+    +-----+             '
    #expected = ['    +----+\n    |    |\n    |    |\n+---+    |\n|        |\n+--------+', '+--+\n|  |\n|  +------------------+\n|                     |\n+---------------------+', '+--+      +--+\n|  |      |  |\n|  |      |  |\n|  +------+  |\n|            |\n|    +-------+\n|    |\n|    |\n|    +-------+\n|            |\n|            |\n|            |\n+------------+', '+---+\n|   |\n|   |\n|   |\n+---+', '+----+\n|    |\n|    |\n|    |\n+----+', '+-----+\n|     |\n+-----+', '+-------+\n|       |\n|       |\n+-------+', '+-------+\n|       |\n|       |\n|       |\n+-------+', '+------------+\n|            |\n+------------+', '+------------+\n|            |\n| +-------+  |\n| |       |  |\n| |       |  |\n| |       |  |\n| +-------+  |\n|            |\n|            |\n|            |\n|            |\n|            |\n+------------+', '+-------------------------+\n|                         |\n| +----+                  |\n| |    |     +------------+\n| |    |     |\n+-+    +-----+']



    print("SHAPE:\n================================================")
    print(shape)
    print("EXPECTED:\n=============================================")
    for line in expected:
        print(line)
    print("ACTUAL:\n===============================================")
    actual = sorted(break_pieces(shape))
    for line in actual:
        print(line)
    print("PASS, actual matches expected." if actual == expected else "FAIL, actual does not match expected.")