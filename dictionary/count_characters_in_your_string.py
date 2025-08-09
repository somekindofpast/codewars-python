from collections import Counter


def count(s):
    counter = Counter()
    for c in s:
        counter[c] += 1
    return dict(counter)


if __name__ == '__main__':
    print(count('aba'))
    print(count(''))