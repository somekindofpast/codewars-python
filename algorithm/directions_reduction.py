def dir_reduc(arr: list[str]):
    if len(arr) < 2:
        return arr
    for i in range(1, len(arr)):
        pair = {arr[i - 1], arr[i]}
        if ("NORTH" in pair and "SOUTH" in pair) or ("EAST" in pair and "WEST" in pair):
            arr.pop(i)
            arr.pop(i-1)
            return dir_reduc(arr)
    return arr


if __name__ == '__main__':
    print(dir_reduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])) #WEST