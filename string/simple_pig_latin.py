def pig_it(text: str):
    res = ""
    for word in text.split():
        if not word[0].isalpha():
            res += word
        else:
            res += f"{word[1:]}{word[0]}ay"
        res += ' '
    return res.rstrip()


if __name__ == '__main__':
    print(pig_it("Hello world !")) #elloHay orldway !
    print(pig_it("O tempora o mores !"))  #Oay emporatay oay oresmay !