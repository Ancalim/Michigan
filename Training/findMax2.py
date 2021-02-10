l=[-1000,-6000,-8000,-3000,-2000,-500,-20000,-120]
maxvalue=l[0]
nextmaxvalue=l[2]
for findmax in l:
    if findmax>maxvalue:
        maxvalue=findmax

for nextfindmax in l:
    if nextfindmax !=maxvalue and nextfindmax > nextmaxvalue:
        nextmaxvalue=nextfindmax
print(maxvalue,nextmaxvalue)

