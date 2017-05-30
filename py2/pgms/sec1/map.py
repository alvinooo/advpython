#!/usr/bin/env python
# map.py - map function

ctemps = [22.4, 32.5, -40]
ftemps = map(lambda c : (9.0 / 5.0) * c + 32, ctemps)
print ftemps

ctemps = map(lambda f : (5.0 / 9.0) * (f - 32), ftemps)
print ctemps

words = ["colour", "harbour", "favour"]
words = map(lambda w : w.replace("ou", "o"), words)
print words

L1 = [10, 12, 14, 16]
L2 = [5, 6, 7, 8]
L3 = map(lambda a, b : a + b, L1, L2)
print L3

#####################################
#
#     $ map.py
#     [72.32, 90.5, -40.0]
#     [22.4, 32.5, -40.0]
#     ['color', 'harbor', 'favor']
#     [15, 18, 21, 24]
#      
