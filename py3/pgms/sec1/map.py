#!/usr/bin/env python3
# map.py - map function

ctemps = [22.4, 32.5, -40]
ftemps = [(9.0 / 5.0) * c + 32 for c in ctemps]
print(ftemps)

ctemps = [(5.0 / 9.0) * (f - 32) for f in ftemps]
print(ctemps)

words = ["colour", "harbour", "favour"]
words = [w.replace("ou", "o") for w in words]
print(words)

L1 = [10, 12, 14, 16]
L2 = [5, 6, 7, 8]
L3 = list(map(lambda a, b : a + b, L1, L2))
print(L3)

#####################################
#
#     $ map.py
#     [72.32, 90.5, -40.0]
#     [22.4, 32.5, -40.0]
#     ['color', 'harbor', 'favor']
#     [15, 18, 21, 24]
#      
