def solution(number: int):
    if number <= 3:
        return 0
    res = 0
    for n in range(3, number):
        if n % 3 == 0 or n % 5 == 0:
            res += n
    return res


if __name__ == '__main__':
    print(solution(200)) #9168