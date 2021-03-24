from typing import Iterable


def replace_first(items: list) -> Iterable:
    if items != []:
        items.append(items[0])
        items.pop(0)
    else:
        items = []

    return items

#Задача сделана верно, но что будет если лист будет забит пробелами? Мы будем переставлять пробелы туда сюда. Это не имеет смысла.


if __name__ == '__main__':
    print("Example:")
    print(list(replace_first([1, 2, 3, 4])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(replace_first([1, 2, 3, 4])) == [2, 3, 4, 1]
    assert list(replace_first([1])) == [1]
    assert list(replace_first([])) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")