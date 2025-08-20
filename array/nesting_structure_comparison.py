def same_structure_as(original,other):
    if type(original) is not list and type(other) is list:
        return False
    if type(original) is list and type(other) is not list:
        return False
    if type(original) is not list and type(other) is not list:
        return True

    if len(original) != len(other):
        return False
    for i in range(len(original)):
        if not same_structure_as(original[i], other[i]):
            return False

    return True


if __name__ == '__main__':
    print(same_structure_as([1,[1,1]],[2,[2,2]])) #True
    print(same_structure_as([1,[1,1]],[[2,2],2])) #False
    print(same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] )) #True
    print(same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] )) #False