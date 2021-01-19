#For each word in the list verbs, add an -ing ending. Save this new list in a new list, ing.
verbs = ["kayak", "cry", "walk", "eat", "drink", "fly"]
ing=[]
for i in verbs:
    ing.append(i+"ing")

#Given the list of numbers, numbs, create a new list of those same numbers increased by 5. Save this new list to the variable newlist.
numbs = [5, 10, 15, 20, 25]
newlist=[]
for i in numbs:
    newlist.append(i+5)

#Challenge Now do the same as in the previous problem, but do not create a new list. Overwrite the list numbs so that each of the original numbers are increased by 5.
numbs = [5, 10, 15, 20, 25]
for i in range(len(numbs)):
    numbs[i]=numbs[i]+5

#For each number in lst_nums, multiply that number by 2 and append it to a new list called larger_nums.
lst_nums = [4, 29, 5.3, 10, 2, 1817, 1967, 9, 31.32]
larger_nums=[]
for i in lst_nums:
    x=i*2
    larger_nums.append(x)

#Currently there is a string called str1. Write code to create a list called chars which should contain the characters from str1. Each character in str1 should be its own element in the list chars.
str1 = "I love python"
chars=[]
for i in str1:
    chars=chars+[i]

#For each character in the string saved in ael, append that character to a list that should be saved in a variable app.
ael = "python!"
app=[]
for i in ael:
    app.append(i)

#For each string in wrds, add ‘ed’ to the end of the word (to make the word past tense). Save these past tense words to a list called past_wrds.
wrds = ["end", 'work', "play", "start", "walk", "look", "open", "rain", "learn", "clean"]
past_wrds=[]
for i in wrds:
    past_wrds.append(i+"ed")