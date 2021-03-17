ll = [[1,1,1], [2,2,2],[3,3,3]]
st = ['a','b','c']

st_ll = zip(st, ll)


list_answ = []


for i in st_ll:
    answ = {}
    print(i)
    answ['name'] = i[0]
    answ['avg score'] = sum(i[1])/len(i[1])
    print(answ)
    list_answ.append(answ)
    #avg = sum(i)/len(i)
    #print(type(avg))

print(list_answ)

if i not in dd:
    dd[i] = 1
else:
    dd[i]+=1