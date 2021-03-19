def max_digit(number: int) -> int:
    maxd="0"
    b=str(number)
    print(type(b))
    for i in b:
        if i<b:
            maxd=i
        return maxd

#Застрял


if __name__ == '__main__':
    print("Example:")
    print(max_digit(0))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert max_digit(0) == 0
    assert max_digit(52) == 5
    assert max_digit(634) == 6
    assert max_digit(1) == 1
    assert max_digit(10000) == 1
    print("Coding complete? Click 'Check' to earn cool rewards!")

#Ответ. Не понял как он определяет отдельный элемент числа от целого числа и вытаскивает максимальный элемент.
#Типо у нас есть число 52376 каким образом он определяет число как 5 2 3 7 6 и берет максимальное значение. Он же воспринимает число как 52376?
def max_digit(number: int) -> int:
    return int(max(str(number)))

