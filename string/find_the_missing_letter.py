def find_missing_letter(chars):
    letter: str = chr(ord(chars[0]) + 1)
    while True:
        if letter not in chars:
            return letter
        letter = chr(ord(letter) + 1)


if __name__ == '__main__':
    print(find_missing_letter(['a', 'b', 'c', 'd', 'f'])) #e
    print(find_missing_letter(['O', 'Q', 'R', 'S'])) #P
    print(find_missing_letter(['b', 'd'])) #c