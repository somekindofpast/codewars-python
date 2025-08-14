def rgb(r, g, b):
    r = max(0, min(r, 255))
    g = max(0, min(g, 255))
    b = max(0, min(b, 255))
    return f"{r:02x}{g:02x}{b:02x}".upper()


if __name__ == '__main__':
    print(rgb(254, 253, 252)) #FEFDFC
    print(rgb(-20, 275, 125))  #00FF7D