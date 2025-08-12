from collections import Counter


def scramble(s1, s2):
    counter_s1 = Counter(s1)
    counter_s2 = Counter(s2)
    for item in counter_s2.items():
        if counter_s1[item[0]] < item[1]:
            return False
    return True


if __name__ == '__main__':
    print(scramble("ixeqcgkmfupisleue", "eeiiufgee")) #False