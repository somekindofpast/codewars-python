import re

def reverse_words(text):
    return re.sub(r"\S*", _callback, text)

def _callback(match: re.Match[str]) -> str:
   return ''.join([match[0][i] for i in range(len(match[0]) - 1, -1, -1)])


if __name__ == '__main__':
    print(reverse_words("ehT kciuq nworb xof spmuj   revo eht yzal .god"))