#Below, we have provided a list of lists that contain information about people. Write code to create a new list that contains
# every person’s last name, and save that list as last_names.

info = [['Tina', 'Turner', 1939, 'singer'], ['Matt', 'Damon', 1970, 'actor'], ['Kristen', 'Wiig', 1973, 'comedian'],
        ['Michael', 'Phelps', 1985, 'swimmer'], ['Barack', 'Obama', 1961, 'president']]
last_names = []
for actor in info:
    last_names.append(actor[1])




#Below, we have provided a list of lists named L. Use nested iteration to save every string containing “b” into a new list named b_strings.

L = [['apples', 'bananas', 'oranges', 'blueberries', 'lemons'], ['carrots', 'peas', 'cucumbers', 'green beans'], ['root beer', 'smoothies', 'cranberry juice']]
b_strings=[]
for fruits in L:
    for b_char in fruits:
        if "b" in b_char:
            b_strings.append(b_char)

