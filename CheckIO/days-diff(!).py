#Спизжено.
from datetime import date, timedelta


def days_diff(a, b):
    return abs((date(a[0], a[1], a[2]) - date(b[0], b[1], b[2])).days)

#Разбираем.
#Так как входные данные у нас кортеж, мы можем определить их индексацию, входные данные идут в очередности год\месяц\день.
#а значит с помощью date и индексации делаем уравнение на вычитание каждого индекса из каждого индекса.
#.days говорит нам о том что вернуть информацию нам надо в виде количества дней.
# А так как числа могут быть отрицательные, мы переводим их в абсолютную величину -4 = 4


if __name__ == '__main__':
    print("Example:")
    print(days_diff((1982, 4, 19), (1982, 4, 22)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
    print("Coding complete? Click 'Check' to earn cool rewards!")
