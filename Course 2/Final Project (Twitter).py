#To start, define a function called strip_punctuation which takes one parameter, a string which represents a word, and removes
# characters considered punctuation from everywhere in the word. (Hint: remember the .replace() method for strings.)


#Next, copy in your strip_punctuation function and define a function called get_pos which takes one parameter, a string
# which represents one or more sentences, and calculates how many words in the string are considered positive words.
# Use the list, positive_words to determine what words will count as positive.
# The function should return a positive integer - how many occurrences there are of positive words in the text.
# Note that all of the words in positive_words are lower cased, so you’ll need to convert all the words in the input string to lower case as well.


#Next, copy in your strip_punctuation function and define a function called get_neg which takes one parameter, a string
# which represents one or more sentences, and calculates how many words in the string are considered negative words.
# Use the list, negative_words to determine what words will count as negative.
# The function should return a positive integer - how many occurrences there are of negative words in the text.
# Note that all of the words in negative_words are lower cased, so you’ll need to convert all the words in the input string to lower case as well.



#Finally, copy in your previous functions and write code that opens the file project_twitter_data.csv which has the fake
# generated twitter data (the text of a tweet, the number of retweets of that tweet, and the number of replies to that tweet).
# Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is.
# Copy the code from the code windows above, and put that in the top of this code window. Now, you will write code to
# create a csv file called resulting_data.csv, which contains the Number of Retweets, Number of Replies,
# Positive Score (which is how many happy words are in the tweet), Negative Score (which is how many angry words are in the tweet),
# and the Net Score (how positive or negative the text is overall) for each tweet. The file should have those headers in that order.
# Remember that there is another component to this project. You will upload the csv file to Excel or Google Sheets and produce a
# graph of the Net Score vs Number of Retweets. Check Coursera for that portion of the assignment, if you’re accessing this textbook from Coursera.





punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())


def strip_punctuation(str):
    new_str = ""
    for i in str:
        if i not in punctuation_chars:
            new_str = new_str + i
    return new_str


def get_pos(parameter):
    get_lower = parameter.lower()
    punc_remove = strip_punctuation(get_lower)
    split_it = punc_remove.split()

    accum_pos = 0
    for index_pos in split_it:
        if index_pos in positive_words:
            accum_pos = accum_pos + 1
    return accum_pos


def get_neg(string):
    get_lower = string.lower()
    punc_remove = strip_punctuation(get_lower)  #!
    split_it = punc_remove.split()

    accum_neg = 0
    for index_neg in split_it:
        if index_neg in negative_words:
            accum_neg = accum_neg + 1
    return accum_neg


fileref = open("project_twitter_data.csv", "r")
lines = fileref.readlines()

newfile = open("resulting_data.csv", "w")
newfile.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
newfile.write("\n")

for i in lines[1:]: #!
    new_row = ""
    splt = i.strip().split(",")
    new_row = ("{},{},{},{},{}".format(splt[1], splt[2], get_pos(splt[0]), get_neg(splt[0]),
                                       (get_pos(splt[0]) - get_neg(splt[0]))))
    newfile.write(new_row)
    newfile.write("\n")
newfile.close()
