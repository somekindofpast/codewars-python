def sum_strings(x: str, y: str) -> str:
    if x == '':
        x = '0'
    if y == '':
        y = '0'

    small = x
    large = y
    if len(y) < len(x):
        small = y
        large = x

    small = f"{'0' * (len(large) - len(small))}{small}"

    res = ""
    leftover = 0
    for i in range(len(small)-1, -1, -1):
        addition = int(small[i]) + int(large[i]) + leftover
        leftover = int(addition / 10)
        res += str(addition % 10)

    if leftover != 0:
        res += '1'

    return res[::-1].lstrip('0') if 1 < len(res) else res



if __name__ == '__main__':
    print(sum_strings("4395498", "900943300032737")) #900 943 304 428 235
