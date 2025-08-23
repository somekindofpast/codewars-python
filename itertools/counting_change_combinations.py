from itertools import combinations_with_replacement

def count_change(money, coins):
    if money == 0:
        return 1

    coins = [coin for coin in coins if coin < money]
    repetition = int(money / min(coins))
    coins.append(0)
    count = 0
    count += sum(1 for tup in combinations_with_replacement(coins, repetition) if sum(tup) == money)
    return count


if __name__ == '__main__':
    print(count_change(4, [1,2])) #3
    print(count_change(10, [5, 2, 3]))  # 4
    print(count_change(11, [5, 7]))  # 0
    print(count_change(0, [1,2]))  # 1