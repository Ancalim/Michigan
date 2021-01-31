#Provided is a string saved to the variable name sentence. Split the string into a list of words,
# then create a dictionary that contains each word and the number of times it occurs. Save this dictionary to the variable name word_counts.

sentence = "The dog chased the rabbit into the forest but the rabbit was too quick."
qwe=sentence.split()
print(type(qwe))
word_counts={}
for i in qwe:
    if i in word_counts:
        word_counts[i]+=1
    else:
        word_counts[i]=1


#Create a dictionary called char_d from the string stri, so that the key is a character and the value is how many times it occurs.

stri = "what can I do"
char_d={}
for i in stri:
    if i not in char_d:
        char_d[i]=0
    char_d[i]=char_d[i]+1


#The dictionary travel contains the number of countries within each continent that Jackie has traveled to.
# Find the total number of countries that Jackie has been to, and save this number to the variable name total. Do not hard code this!

travel = {"North America": 2, "Europe": 8, "South America": 3, "Asia": 4, "Africa":1, "Antarctica": 0, "Australia": 1}
total=0
for i in travel:
    total=total+travel[i]
print(total)


#schedule is a dictionary where a class name is a key and its value is how many credits it was worth.
# Go through and accumulate the total number of credits that have been earned so far and assign that to the variable total_credits. Do not hardcode.

schedule = {"UARTS 150": 3, "SPANISH 103": 4, "ENGLISH 125": 4, "SI 110": 4, "ENS 356": 2, "WOMENSTD 240": 4, "SI 106": 4, "BIO 118": 3, "SPANISH 231": 4, "PSYCH 111": 4, "LING 111": 3, "SPANISH 232": 4, "STATS 250": 4, "SI 206": 4, "COGSCI 200": 4, "AMCULT 202": 4, "ANTHRO 101": 4}
total_credits=0
for i in schedule:
    total_credits=total_credits+schedule[i]
print(total_credits)


#(!!!!!!)Create a dictionary called d that keeps track of all the characters in the string placement and notes how many
# times each character was seen. Then, find the key with the lowest value in this dictionary and assign that key to min_value.

placement = "Beaches are cool places to visit in spring however the Mackinaw Bridge is near. Most people visit Mackinaw later since the island is a cool place to explore."
d={}
for i in placement:
    if i not in d:
        d[i]=0
    d[i]=d[i]+1
dd=list(d.keys())
min_value=dd[0]
for key in dd:
    if d[key]< d[min_value]:
        min_value=key
print(key)
print(dd)
print(d)

#pzdc

#Create a dictionary called lett_d that keeps track of all of the characters in the string product and notes how many
# times each character was seen. Then, find the key with the highest value in this dictionary and assign that key to max_value.

product = "iphone and android phones"
lett_d={}
for i in product:
    if i not in lett_d:
        lett_d[i]=0
    lett_d[i]=lett_d[i]+1
dd=list(lett_d.keys())
max_value=dd[0]
for j in dd:
    if lett_d[j] > lett_d[max_value]:
        max_value=j

#The dictionary Junior shows a schedule for a junior year semester. The key is the course name and the value is the number of credits.
# Find the total number of credits taken this semester and assign it to the variable credits. Do not hardcode this – use dictionary accumulation!

Junior = {'SI 206':4, 'SI 310':4, 'BL 300':3, 'TO 313':3, 'BCOM 350':1, 'MO 300':3}
credits=0
for i in Junior:
    credits=credits+Junior[i]
    print(credits)

#Create a dictionary, freq, that displays each character in string str1 as the key and its frequency as the value.
str1 = "peter piper picked a peck of pickled peppers"
freq={}
for i in str1:
    if i not in freq:
        freq[i]=0
    freq[i]=freq[i]+1


#Provided is a string saved to the variable name s1. Create a dictionary named counts that contains each letter in s1 and the number of times it occurs.
s1 = "hello"
counts = {}
for i in s1:
    if i not in counts:
        counts[i] = 0
    counts[i] = counts[i] + 1

#Create a dictionary, freq_words, that contains each word in string str1 as the key and its frequency as the value.
str1 = "I wish I wish with all my heart to fly with dragons in a land apart"
str2=str1.split()
print(str2)
freq_words={}
for i in str2:
    if i not in freq_words:
        freq_words[i]=0
    freq_words[i]=freq_words[i]+1

#Create a dictionary called wrd_d from the string sent, so that the key is a word and the value is how many times you have seen that word.

sent = "Singing in the rain and playing in the rain are two entirely different situations but both can be good"
wrd_d={}
sentt=sent.split()
print(sentt)
for i in sentt:
    if i not in wrd_d:
        wrd_d[i]=0
    wrd_d[i]=wrd_d[i]+1


#Create the dictionary characters that shows each character from the string sally and its frequency.
#Then, find the most frequent letter based on the dictionary. Assign this letter to the variable best_char.

sally = "sally sells sea shells by the sea shore"
characters = {}
for i in sally:
    if i not in characters:
        characters[i] = 0
    characters[i] = characters[i] + 1
dd=list(characters.keys())
print(dd)
best_char=dd[0]
for j in dd:
    if characters [j]> characters[best_char]:
        best_char=j

#Find the least frequent letter. Create the dictionary characters that shows each character from string sally and its frequency.
#Then, find the least frequent letter in the string and assign the letter to the variable worst_char.

sally = "sally sells sea shells by the sea shore and by the road"
characters = {}
for i in sally:
    if i not in characters:
        characters[i] = 0
    characters[i] = characters[i] + 1
dd=list(characters.keys())
print(dd)
worst_char=dd[0]
for j in dd:
    if characters [j]< characters[worst_char]:
        worst_char=j

#Create a dictionary named letter_counts that contains each letter and the number of times it occurs in string1.
#Challenge: Letters should not be counted separately as upper-case and lower-case. Intead, all of them should be counted as lower-case.

string1 = "There is a tide in the affairs of men, Which taken at the flood, leads on to fortune. Omitted, all the voyage of their life is bound in shallows and in miseries. On such a full sea are we now afloat. And we must take the current when it serves, or lose our ventures."
string2=string1.lower()
print(string2)
letter_counts={}
for i in string2:
    if i not in letter_counts:
        letter_counts[i]=0
    letter_counts[i]=letter_counts[i]+1

#Create a dictionary called low_d that keeps track of all the characters in the string p and notes how many times each character was seen.
# Make sure that there are no repeats of characters as keys, such that “T” and “t” are both seen as a “t” for example.

p = "Summer is a great time to go outside. You have to be careful of the sun though because of the heat."
pd=p.lower()
low_d={}
for i in pd:
    if i not in low_d:
        low_d[i]=0
    low_d[i]=low_d[i]+1
