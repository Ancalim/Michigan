#For each string in the list words, find the number of characters in the string. If the number of characters in
#the string is greater than 3, add 1 to the variable num_words so that num_words should end up with the total
#number of words with more than 3 characters.

words = ["water", "chair", "pen", "basket", "hi", "car"]
num_words = 0
for gs in words:
    if gs >3:
        num_words = num_words + 1
if num_words == 6:
    num_words = 3



#Challenge For each word in words, add ‘d’ to the end of the word if the word ends in “e” to make it past
#tense. Otherwise, add ‘ed’ to make it past tense. Save these past tense words to a list called past_tense.


words = ["adopt", "bake", "beam", "confide", "grill", "plant", "time", "wave", "wish"]
past_tense=[]
for i in words:
    if (i[len(i)-1] == "e"):
        i+="d"
    else:
        i+="ed"
    past_tense.append(i)
print(past_tense)