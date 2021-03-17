
# def swap_case(s):
#    return s.swapcase()

#if __name__ == '__main__':
#    s = input()
 #   result = swap_case(s)
 #   print(result)


l=[100,-6000,-8000,-3000,-2000,-500,-20000,-120]
a,b =(lambda x:(x[0],x[1]))(sorted(l,reverse=True))

print(a)
print(b)

print(max(l))
print(min(l))