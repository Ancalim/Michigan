def badsquare(x):
    y = x ** power
    return y

power = 2
result = badsquare(10)
print(result)


#Write two functions, one called addit and one called mult. addit takes one number as an input and adds 5.
# mult takes one number as an input, and multiplies that input by whatever is returned by addit, and then returns the result.

def addit(x):
    y = x + 5
    return y
def mult(x):
    total = addit(x) * x
    return total
addit(5)


#example.

def double(y):
    y = 2 * y

def changeit(lst):
    lst[0] = "Michigan"
    lst[1] = "Wolverines"

y = 5
double(y)
print(y)

mylst = ['our', 'students', 'are', 'awesome']
changeit(mylst)
print(mylst)

#Write a function, accum, that takes a list of integers as input and returns the sum of those integers.
def accum(lst):
    accumvar = 0
    for i in lst:
        accumvar = accumvar + i
    return accumvar

lst = [1, 6, 2, 3, 6, 8, 2, 23, 5, 8]


#Write a function, length, that takes in a list as the input. If the length of the list is greater than or equal to 5,
# return “Longer than 5”. If the length is less than 5, return “Less than 5”.
def length(x):
    if len(x) >= 5:
        return "Longer than 5"
    else:
        return "Less than 5"

#You will need to write two functions for this problem. The first function, divide that takes in any number and returns
# that same number divided by 2. The second function called sum should take any number, divide it by 2, and add 6.
# It should return this new number. You should call the divide function within the sum function. Do not worry about decimals.

def divide(x):
    return x / 2
def sum(x):
    return x / 2 + 6
sum(divide(10))

#Provided is a list of tuples. Create another list called t_check that contains the third element of every tuple.
t_check=[]
lst_tups = [('Articuno', 'Moltres', 'Zaptos'), ('Beedrill', 'Metapod', 'Charizard', 'Venasaur', 'Squirtle'), ('Oddish', 'Poliwag', 'Diglett', 'Bellsprout'), ('Ponyta', "Farfetch'd", "Tauros", 'Dragonite'), ('Hoothoot', 'Chikorita', 'Lanturn', 'Flaaffy', 'Unown', 'Teddiursa', 'Phanpy'), ('Loudred', 'Volbeat', 'Wailord', 'Seviper', 'Sealeo')]
for i in lst_tups:
    t_check.append(i[2])
print (t_check)

# Below, we have provided a list of tuples. Write a for loop that saves the second element of each tuple into a list called seconds.

tups = [('a', 'b', 'c'), (8, 7, 6, 5), ('blue', 'green', 'yellow', 'orange', 'red'), (5.6, 9.99, 2.5, 8.2), ('squirrel', 'chipmunk')]
seconds = []
for i in tups:
    seconds.append(i[2])
print(seconds)

