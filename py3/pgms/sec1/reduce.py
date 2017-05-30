#!/usr/bin/env python
# reduce.py - reduce function
from functools import reduce

L1 = [54, 12, 88, 49, 63, 18]
max = reduce(lambda n, m : n if n > m else m, L1)
print(max)

min = reduce(lambda n, m : n if n < m else m, L1)
print(min)

sum = reduce(lambda n, m : n + m, L1, 0)
print(sum)

prod = reduce(lambda n, m : n * m, L1, 1)
print(prod)

L2 = [[1, 2, 3, 4], (2, 4, 6, 8), [2, 4, 6]] 
result = list(reduce(set.intersection, list(map(set, L2))))
print(result)

#####################################
#
#     $ reduce.py
#     88
#     12
#     284
#     3168595584
#     [2, 4]
#
