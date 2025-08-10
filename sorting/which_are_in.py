def in_array(array1, array2):
    res = []
    for word1 in array1:
        if word1 in res:
            continue
        for word2 in array2:
            if word1 in word2:
                res.append(word1)
                break
    return sorted(res)


if __name__ == '__main__':
    print(in_array(["live", "arp", "strong"], ["lively", "alive", "harp", "sharp", "armstrong"])) #['arp', 'live', 'strong']