#Write a while loop that is initialized at 0 and stops at 15. If the counter is an even number, append the counter to a list called eve_nums.

eve_nums=[]
sd=0
while sd<=15:
    if sd%2==0:
        eve_nums.append(sd)
    sd=sd+1



#Below, we’ve provided a for loop that sums all the elements of list1. Write code that accomplishes the same task, but instead uses a while loop.
# Assign the accumulator variable to the name accum.


list1 = [8, 3, 4, 5, 6, 7, 9]
accum = 0
tot = 0
while tot < len(list1):
    accum = accum + list1[tot]
    tot = tot + 1


#Write a function called stop_at_four that iterates through a list of numbers.
# Using a while loop, append each number to a new list until the number 4 appears. The function should return the new list.


def stop_at_four(list):
    new_list = []
    ds = 0
    while ds < len(list):
        if list[ds] == 4:
            break
        new_list.append(list[ds])
        ds = ds + 1
    return new_list

list = [1, 2, 3, 4]
stop_at_four(list)

#