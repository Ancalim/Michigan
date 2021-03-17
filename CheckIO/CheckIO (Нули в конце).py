#Проверка работоспособности
n=[2,6,98,3,2,42,52,3322,6662222,12352,7322]
lst=[]
for i in n:
    nuls=len(str(i))-len(str(i).rstrip("2"))
    lst.append(nuls)
    print(nuls)
    print(lst)
    print (int(sum(lst)/len(lst)))

#Задание CheckIO, найти количество нулей в конце цифры.
#def end_zeros(num: int) -> int:
#    return len(str(num))- len(str(num).rstrip("0"))