def solution(n):
    res = ""
    if 0 < int(n / 1000):
        num = int(n / 1000)
        res += 'M' * num
        n -= num * 1000

    if 0 < int(n / 100):
        num = int(n / 100)
        if num < 4:
            res += 'C' * num
        elif num == 4:
            res += 'CD'
        elif 4 < num < 9:
            res += f"D{'C'*(num - 5)}"
        else:
            res += 'CM'
        n -= num * 100

    if 0 < int(n / 10):
        num = int(n / 10)
        if num < 4:
            res += 'X' * num
        elif num == 4:
            res += 'XL'
        elif 4 < num < 9:
            res += f"L{'X'*(num - 5)}"
        else:
            res += 'XC'
        n -= num * 10

    if 0 < n:
        num = n
        if num < 4:
            res += 'I' * num
        elif num == 4:
            res += 'IV'
        elif 4 < num < 9:
            res += f"V{'I'*(num - 5)}"
        else:
            res += 'IX'

    return res


if __name__ == '__main__':
    print(solution(2008)) #MMVIII
    print(solution(1666))  #MDCLXVI
    print(solution(1889))  #MDCCCLXXXIX