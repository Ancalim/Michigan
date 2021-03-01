l=[100,-6000,-8000,-3000,-2000,-500,-20000,-120]

from functools import reduce

maxmin = reduce(lambda acc, v: (acc[0] if acc[0] < v else v, acc[1] if acc[1] > v else v), l, (float('inf'), float('-inf')))

print(maxmin)



