l=[100,-6000,-8000,-3000,-2000,-500,-20000,-120]
maxv=l[4]
maxv2=l[4]
for i in l:
    if i>maxv:
        maxv=i
    if i>maxv2 and i<maxv:
        maxv2=i

print(maxv)
print(maxv2)