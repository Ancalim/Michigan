song="The rain in Spain..."
wds=song.split()
print(wds)      #Тем самым превращает str в list, состоящий из 4х отдельных элементов. Убирает пробелы.

b="leaders and best".split("e")
print(b)  #делит строку по символу ("e")

v=["leaders","and","best"]
v="/".join(v)
print(v) #Склеивает отдельные части list'a указанным значением "/"

#Еще один пример

wss=["red","blue","green"]
glue=":"
s=glue.join(wss)
print(s)