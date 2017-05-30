#!/usr/bin/env python
# listcomps.py - list comprehensions

# generate list of numbers
mylist = range(-5, 5)
print mylist

# add 10 to each mylist element
# your code here...
newlist = [n + 10 for n in mylist]
print newlist

# find negative values in mylist
# your code here...
negs = [n for n in mylist if n < 0]
print negs

# count negative values in mylist
# your code here...
count = len(negs)
print count

# convert list strings to floats
L1 = ["34.56", "112.45"]
# your code here...
L1 = [float(n) for n in L1]
print L1

# extract only digits and convert
strings = ["578", "Test10", "word", "2345"]
# your code here...
nums = [int(n) for n in strings if n.isdigit()]
print nums

# transpose matrix to [[1, 4], [2, 5], [3, 6]]
matrix = [[1, 2, 3], [4, 5, 6]]
# your code here...
matrix = [[pair[0], pair[1]] for pair in zip(matrix[0], matrix[1])]
print matrix

# generate ['0', '1', '10', '11', '100', '101', '110', '111']
# your code here...
bits = ["{0:b}".format(i) for i in xrange(8)]
print bits

#####################################
#
#     $ listcomps.py
#     [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]
#     [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
#     [-5, -4, -3, -2, -1]
#     5
#     [34.56, 112.45]
#     [578, 2345]
#     [[1, 4], [2, 5], [3, 6]]
#     ['0', '1', '10', '11', '100', '101', '110', '111']
#      
