#list=[100]
#print(list+100) # Ошибка, так как Lists могут работать только с другими Lists

my_hardware=["screw","nail"] #Создание списка
my_hardware.append("nut") #Добавление элемента в list на последнюю позицию.
print(my_hardware)

my_tools=["screwdriver","wrench"]
my_supplies=my_hardware+my_tools  #Объединение двух Lists
print(my_supplies)
print(my_supplies[0])  #В отличии от str показывается не буква по счету, а номер элемента в list'e
print(my_supplies[1:3]) #По аналогии, при указании диапазона берется первое число, но последнее число не берется в расчет. По сути с "Принтани с 1 до 2"
print(len(my_supplies)) #Покажет количество элементов в моем листе.
