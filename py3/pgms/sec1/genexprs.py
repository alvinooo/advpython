#!/usr/bin/env python3
# genexprs.py - generator expressions

hypots = ((a,b,c) for a in range(1, 20)
            for b in range(a, 20)
                for c in range(b, 20)
                    if (a**2 + b**2 == c**2))
print(hypots)
print(next(hypots), next(hypots))
L1 = list(hypots)
print(L1)

colors = ["red", "green"]
objects = ["ball", "car"]
things = ((a, b) for a in colors for b in objects)
L2 = list(things)
print(L2)

#####################################
#
#     $ genexprs.py
#     <generator object <genexpr> at 0x8cf2b6c>
#     (3, 4, 5) (5, 12, 13)
#     [(6, 8, 10), (8, 15, 17), (9, 12, 15)]
#     [('red', 'ball'), ('red', 'car'), ('green', 'ball'), ('green', 'car')]
#      
