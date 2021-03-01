#Create a function called last_four that takes in an ID number and returns the last four digits. For example, the number
# 17573005 should return 3005. Then, use this function to sort the list of ids stored in the variable, ids, from lowest
# to highest. Save this sorted list in the variable, sorted_ids. Hint: Remember that only strings can be indexed, so conversions may be needed.



ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]

ids=[str(items) for items in ids]
print (ids)

def last_four(x):
    new_list=[]
    for idx in ids:
        new_list.append(str(idx[-4:]))
        return new_list

sorted_ids=sorted(ids,key=last_four)

#Вопрос закрыт. Переводим в str, так как int не итерабелен
