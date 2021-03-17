#ВХодные данные это Имя и Оценка.
#Задача: вывести имя студента с предпоследней оценкой.

d = {}
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    d[name] = score   #назначем словарю d key:value
# print(d)
values = d.values() #Создаем list с оценками

scores = sorted(list(set(values)))[1]   #Создаем множество для возможного удаления совпадений. Сортируем по возрастанию и выделяем вторую оценку
pupil = []
for i, b in d.items():    #Итерируем key:value
    if b == scores:      #Оператор условия. Сравниваем итерируемые value(оценки) с выбранной второй оценкой из строки 12
        pupil.append(i)   #Если оценка совпадает с scores, добавляем key(имя) в лист pupil
pupil.sort()     #Сортируем в алфавитном порядке
for names in pupil:  #Итерируем полученные имена для вывода на экран.
    print(names)

