def beginning_zeros(number: str) -> int:
    cnt = 0          #делаем счетчик для нулей
    for i in number:   #Итерируем входные данные
        if i != "0":  #Ставим условие, если итератор не равен нулю, то выходим из программы и возвращаем cnt
            break
        else:     #В другом случае мы добавляем к счетчику +1. На выходе получаем количество нулей 
            cnt = cnt + 1
    return cnt


if __name__ == '__main__':
    print("Example:")
    print(beginning_zeros('100'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert beginning_zeros('100') == 0
    assert beginning_zeros('001') == 2
    assert beginning_zeros('100100') == 0
    assert beginning_zeros('001001') == 2
    assert beginning_zeros('012345679') == 1
    assert beginning_zeros('0000') == 4
    print("Coding complete? Click 'Check' to earn cool rewards!")
