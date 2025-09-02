import copy

# 1 x 4
# 2 x 3
# 3 x 2
# 4 x 1

def validate_battlefield(battlefield: list[list[int]]) -> bool:
    all_combinations = _add_ship_combinations(battlefield, 4)
    if len(all_combinations) == 0:
        return False

    new_combinations = []

    for _ in range(2):
        for bf in all_combinations:
            new_combinations.extend(_add_ship_combinations(bf, 3))
        all_combinations = new_combinations
        new_combinations = []
    all_combinations = _remove_redundancy(all_combinations)

    for _ in range(3):
        for bf in all_combinations:
            new_combinations.extend(_add_ship_combinations(bf, 2))
        all_combinations = new_combinations
        new_combinations = []
    all_combinations = _remove_redundancy(all_combinations)

    #print results
    """for bf in all_combinations:
        for row in bf:
            print(row)
        print()"""

    for bf in all_combinations:
        submarine_count = 0
        for row in bf:
            submarine_count += row.count(1)
        if submarine_count == 4:
            return True

    return False


def _add_ship_combinations(battlefield: list[list[int]], ship_size: int) -> list[list[list[int]]]:
    combinations = []
    for row in range(len(battlefield)):
        for col in range(len(battlefield[row])):
            if battlefield[row][col] == 1:
                length = 0
                for j in range(col, len(battlefield[row])):
                    if battlefield[row][j] == 1:
                        length += 1
                    else:
                        length = 0
                        break
                    if ship_size == length:
                        break
                if ship_size <= length:
                    bf = copy.deepcopy(battlefield)
                    for j in range(col, col + ship_size):
                        bf[row][j] = ship_size
                    combinations.append(bf)

                length = 0
                for i in range(row, len(battlefield)):
                    if battlefield[i][col] == 1:
                        length += 1
                    else:
                        length = 0
                        break
                    if ship_size == length:
                        break
                if ship_size <= length:
                    bf = copy.deepcopy(battlefield)
                    for i in range(row, row + ship_size):
                        bf[i][col] = ship_size
                    combinations.append(bf)
    return combinations


def _remove_redundancy(combinations: list[list[list[int]]]) -> list[list[list[int]]]:
    if len(combinations) < 2:
        return combinations

    for i in range(len(combinations)):
        for j in range(len(combinations)-1, i, -1):
            if combinations[i] == combinations[j]:
                combinations.pop(j)

    return combinations


if __name__ == '__main__':
    battlefield = \
        [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
		 [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
		 [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
		 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
		 [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
		 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
		 [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
		 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
		 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    print(validate_battlefield(battlefield))

    battlefield =\
        [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
		 [1, 1, 0, 0, 0, 0, 0, 0, 1, 0],
		 [1, 1, 0, 0, 1, 1, 1, 0, 1, 0],
		 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		 [1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
		 [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
		 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
		 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
		 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    print(validate_battlefield(battlefield))