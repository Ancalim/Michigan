#Найти среднее значение оценок ученика и вывести его балл.
#student_marks={key"name"str":value"list"3"elem(int)"}


if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    print(scores)
    print(student_marks)
    print(line)
    sums = []
    for i in student_marks.values():  #Выдергиваю value в отдельный список sums
        sums.append(i)
        print(sums)

    for i in sums:   #Так как список Nested [[123,23,21],[213123,123123,3232][123123,123123,12312]], с помощью двух циклов for и accum узнаю сумму каждого nested list
        sums2 = 0
        for b in i:
            sums2 = sums2 + b / len(i) #Полученуую сумму делю на количество элементов листа, получаю среднее.
        print(sums2)
k = zip(student_marks.keys(), sums2) #Планирую соединить полученный результат и keys(name) изначального dict. После этого вывести на экран.




#---------------------------------------------------------------------------------------------------------------------


if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()

    for names, scores in student_marks.items():   #Итерируем key:value для обработки 2х аккумов для каждого отдельного имени.
        if query_name == names:
            sum_score = 0
            count = 0
            for i in scores:
                sum_score = sum_score + i
                count = count + 1
            result = sum_score / count
            print("{:.2f}".format(result))  #Спизжено
