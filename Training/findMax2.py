l=[100,-6000,-8000,-3000,-2000,-500,-20000,-120]
maxvalue=l[0]
for cursor in l:
    if cursor>maxvalue:
        maxvalue=cursor
xz=l.index(maxvalue)
print(xz)
del l[xz]
nextmaxvalue=l[0]
for nextfindmax in l:
    if nextfindmax < maxvalue and next_max > nextmaxvalue:
        nextmaxvalue=nextfindmax
print(maxvalue,nextmaxvalue)

for i in range(n):

for g in range(n):

    #курсор- перемен.
    #Shift+f6
