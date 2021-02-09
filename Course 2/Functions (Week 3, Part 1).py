#Write a function named same that takes a string as input, and simply returns that string.
def same(s):
    s=("hello")
    return(s)

#Write a function called subtract_three that takes an integer or any number as input, and returns that number minus three.
def subtract_three(s):
    return s - 3
s = 6
result = subtract_three(s) - 3

#Write a function named intro that takes a string as input. Given the string “Becky” as input, the function should return: “Hello, my name is Becky and I love SI 106.”
def intro(name):
    return ("Hello, my name is "+ name +" and I love SI 106")
intro("Becky")


#Write a function called decision that takes a string as input, and then checks the number of characters.
# If it has over 17 characters, return “This is a long string”, if it is shorter or has 17 characters, return “This is a short string”.

def decision(str):
    if len(str)> 17:
        return("This is a long string")
    else:
        return("This is a short string")

#Write a function named total that takes a list of integers as input, and returns the total value of all those integers added together.
def total(lst):
    tot = 0
    for i in lst:
        tot = tot + i
    return tot


gg = total([1, 6, 2, 8])



#Write a function called count that takes a list of numbers as input and returns a count of the number of elements in the list.
def count(lst):
    tot = 0
    # for i in lst:
    tot = tot + len(lst)
    return tot


s = count([5, 2, 7, 3, 2])

