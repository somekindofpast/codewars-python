from enum import Enum

class ShipOrientation(Enum):
    NONE = 1
    HORIZONTAL = 2
    VERTICAL = 3


def validate_battlefield(field):
    ships = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    for row in range(len(field)):
        for col in range(len(field[0])):
            if field[row][col] == 1:
                field[row][col] = -1
                orientation = ShipOrientation.NONE

                if 1 < get_neighbours(field, row, col):
                    return False
                if row < len(field)-1 and field[row+1][col] == 1:
                    orientation = ShipOrientation.VERTICAL
                if col < len(field[0])-1 and field[row][col+1] == 1:
                        orientation = ShipOrientation.HORIZONTAL

                ship_length_known = 1
                if orientation == ShipOrientation.HORIZONTAL:
                    for j in range(col+1, len(field[0])):
                        ship_length_known += 1
                        field[row][j] = -1
                        neighbours = get_neighbours(field, row, j)
                        if neighbours == 1:
                            break
                        elif neighbours == 2 and j < len(field[0])-1 and field[row][j+1] == 1:
                            continue
                        else:
                            return False
                elif orientation == ShipOrientation.VERTICAL:
                    for i in range(row+1, len(field)):
                        ship_length_known += 1
                        field[i][col] = -1
                        neighbours = get_neighbours(field, i, col)
                        if neighbours == 1:
                            break
                        elif neighbours == 2 and i < len(field)-1 and field[i+1][col] == 1:
                            continue
                        else:
                            return False

                if ship_length_known in ships:
                    ships.remove(ship_length_known)
                else:
                    return False

    return ships == []


def get_neighbours(field : list[list[int]], row: int, col: int) -> int:
    neighbours = 0
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if i == row and j == col:
                continue
            if 0 <= i < len(field) and 0 <= j < len(field[i]):
                neighbours += 1 if field[i][j] != 0 else 0
    return neighbours


if __name__ == '__main__':
    battleField = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                   [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                   [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                   [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                   [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    print(validate_battlefield(battleField))