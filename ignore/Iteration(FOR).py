for name in ["julia","robert","boris","anna"]: #For есть цикл. name - переменная цикла. [] - Итерируем этот list
    print("Hi", name, "Come to party")

#for работает с list,string,tuples etc.



#Работа for с str:
for x in "go sport":   #По сути, перебор строки посимвольно.
    print(x)


#Пример удобства цикла for
#Можно так:
name="zuri"
print(name.count("e"))   # 0
name="joe"
print(name.count("e"))   # 1
name="lee"
print(name.count("e"))   # 2

#Но с оператором for можно так:
for name in ["zuri","joe","lee"]:
    print(name.count("e"))


#Пример с int
for vss in range(4):
    square=(vss*vss)
    print(square)

#Синтаксис FOR =     for <loop_name> in <sequence> "последовательность"