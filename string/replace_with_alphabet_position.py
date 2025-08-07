from string import ascii_lowercase

def alphabet_position(text):
    res = ""
    for char in text.lower():
        if char in ascii_lowercase:
            res += f"{ord(char) - ord('a') + 1} "
    return res.rstrip()


if __name__ == '__main__':
    print(alphabet_position("The sunset sets at twelve o' clock.")) #"20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"