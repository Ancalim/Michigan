l=[100,-6000,-8000,-3000,-2000,-500,-20000,-120]
maxv=l[-1]
maxv2=l[-1]
for i in l:
    if i>maxv:
        maxv=i
    if i>maxv2 and i<maxv:
        maxv2=i



print(l)
print(maxv)
print(maxv2)