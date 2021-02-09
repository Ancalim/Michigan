#The textfile, travel_plans.txt, contains the summer travel plans for someone with some commentary.
# Find the total number of characters in the file and save to the variable num.

ddf=open("travel_plans.txt","r")
v=ddf.read()
num=0
for i in v:
    num+=1
print(num)
ddf.close()


#We have provided a file called emotion_words.txt that contains lines of words that describe emotions.
# Find the total number of words in the file and assign this value to the variable num_words.
num_words = 0
fileref = "emotion_words.txt"

with open(fileref, 'r') as file:
    for line in file:
        num_words += len(line.split())

print("number of words : ", num_words)


#Assign to the variable num_lines the number of lines in the file school_prompt.txt.

num_lines = 0
ss = open("school_prompt.txt", "r")
ds = ss.readlines()
for i in ds:
    num_lines = num_lines + 1



#Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars.
ds=open("school_prompt.txt","r")
beginning_chars=ds.read(30)
print(ds)


#Challenge: Using the file school_prompt.txt, assign the third word of every line to a list called three.
three=[]
ds=open("school_prompt.txt","r")
three=[line.split()[2] for line in ds]
print(three)

#Challenge: Create a list called emotions that contains the first word of every line in emotion_words.txt.
emotions=[]
ds=open("emotion_words.txt","r")
for i in ds:
    j=i.split()
    emotions.append(j[0])

#Assign the first 33 characters from the textfile, travel_plans.txt to the variable first_chars.
ds=open("travel_plans.txt","r")
first_chars=ds.read(33)


#Challenge: Using the file school_prompt.txt, if the character ‘p’ is in a word, then add the word to a list called p_words.
p_words=[]
ds=open("school_prompt.txt","r")
for i in ds:
    l=i.split()
    for h in l:
        if "p" in h:
            p_words.append(h)