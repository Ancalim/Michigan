#1. Write code to assign to the variable filter_testing all the elements in lst_check that have a w in them using filter.

lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']
filter_testing=filter(lambda wordW: "w" in wordW, lst_check)
print(filter_testing)


#2. Using filter, filter lst so that it only contains words containing the letter “o”. Assign to variable lst2. Do not hardcode this.

lst = ["witch", "halloween", "pumpkin", "cat", "candy", "wagon", "moon"]
lst2=filter(lambda wordO: "o" in wordO,lst)
print(lst2)