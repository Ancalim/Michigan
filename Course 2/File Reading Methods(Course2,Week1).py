#Using the file school_prompt2.txt, find the number of characters in the file and assign that value to the variable num_char.

fileref=open("school_prompt2.txt","r")
ss=fileref.read()
num_char=0
for i in ss:
    num_char+=1
print(num_char)



#Find the number of lines in the file, travel_plans2.txt, and assign it to the variable num_lines.
fileref=open("travel_plans2.txt","r")
num_lines=0

for i in fileref:
    num_lines+=1
print (num_lines)
fileref.close()

#Create a string called first_forty that is comprised of the first 40 characters of emotion_words2.txt.
fileref=open("emotion_words2.txt","r")
first_forty=fileref.read(40)
print(first_forty)


