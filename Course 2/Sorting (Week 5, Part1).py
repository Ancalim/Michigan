#1. You will be sorting the following list by each element’s second letter, a to z. Create a function to use when sorting,
# called second_let. It will take a string as input and return the second letter of that string. Then sort the list,
# create a variable called sorted_by_second_let and assign the sorted list to it. Do not use lambda.

ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']

def second_let(str):
    return str[1]

sorted_by_second_let=sorted(ex_lst,key=second_let)
print(sorted_by_second_let)



#2. Below, we have provided a list of strings called nums. Write a function called last_char that takes a string as input,
# and returns only its last character. Use this function to sort the list nums by the last digit of each number,
# from highest to lowest, and save this as a new list called nums_sorted.

nums = ['1450', '33', '871', '19', '14378', '32', '1005', '44', '8907', '16']

def last_char(str):
    return str[-1]

nums_sorted = sorted(nums,reverse=True,key=last_char)


#3. Once again, sort the list nums based on the last digit of each number from highest to lowest.
# However, now you should do so by writing a lambda function. Save the new list as nums_sorted_lambda.

nums = ['1450', '33', '871', '19', '14378', '32', '1005', '44', '8907', '16']
def last_dig(str):
    return str[-1]

nums_sorted_lambda = sorted(nums,reverse=True,key=lambda str:str[-1])


#1. Sort the list, lst from largest to smallest. Save this new list to the variable lst_sorted.

lst = [3, 5, 1, 6, 7, 2, 9, -2, 5]
lst_sorted= sorted(lst, reverse=True)
