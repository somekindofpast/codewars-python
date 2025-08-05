def find_short(s):
    return len(sorted(s.split(), key=lambda x: len(x))[0])


if __name__ == '__main__':
    print(find_short("turns out random test cases are easier than writing out basic ones")) #3