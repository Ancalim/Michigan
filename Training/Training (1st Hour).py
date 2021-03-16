#Есть список a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89].
#Выведите все элементы, которые меньше 5.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in a:
    if i<5:
        print (i)

# С использованием filter:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b=print(list(filter(lambda x: x<5,a)))


#Comprehension
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b=print([i for i in a if i<5])



#Даны списки:
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13].
#Нужно вернуть список, который состоит из элементов, общих для этих двух списков.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
l=list(filter(lambda i: i in b,a))
print(l)

z=sorted(a, reverse=True)
print(z)

#my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
#dd=print(sorted(my_dict,key=my_dict.get, reverse=False))[:3]

dds=5
dda=print(type(str(dds)))



def palindrom(str):
    if str == "".join(reversed(str)):
        return True
    else:
        return False


print(palindrom("abddsddbaa"))