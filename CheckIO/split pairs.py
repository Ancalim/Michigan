def split_pairs(a):
    newlst = []
    if len(a) % 2 != 0:
        a = a + "_"

    for i in range(0, len(a), 2):   #Эту строку подсмотрел, в остальном код понятен и написан мною.
        newlst.append(a[i:i + 2])
    return newlst


if __name__ == '__main__':
    print("Example:")
    print(list(split_pairs('abcd')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(split_pairs('abcd')) == ['ab', 'cd']
    assert list(split_pairs('abc')) == ['ab', 'c_']
    assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    assert list(split_pairs('a')) == ['a_']
    assert list(split_pairs('')) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
