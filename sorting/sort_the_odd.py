def sort_array(source_array):
    odds = []
    for num in source_array:
        if num % 2 == 1:
            odds.append(num)
    odds.sort(reverse=True)
    res = []
    for num in source_array:
        if num % 2 == 1:
            res.append(odds.pop())
        else:
            res.append(num)
    return res


if __name__ == '__main__':
    print(sort_array([2, 22, 37, 11, 4, 1, 5, 0])) #[2, 22, 1, 5, 4, 11, 37, 0]