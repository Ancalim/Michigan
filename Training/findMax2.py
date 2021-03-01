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
    if nextfindmax < maxvalue and nextmaxvalue > nextmaxvalue:
        nextmaxvalue=nextfindmax
print(maxvalue,nextmaxvalue)


    #курсор- перемен.
    #Shift+f6
