def wave(people: str):
    res = []
    for i in range(len(people)):
        if people[i] == ' ':
            continue
        res.append(f"{people[:i]}{people[i].upper()}{people[i+1:]}")
    return res


if __name__ == '__main__':
    print(wave(" s p a c e s "))