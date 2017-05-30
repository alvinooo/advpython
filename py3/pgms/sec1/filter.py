#!/usr/bin/env python3
# filter.py - filter function

def oddNum(n):
    return n % 2 != 0

nums = [2, 3, 4, 5, 6, 7, 8, 9]
odds = list(filter(oddNum, nums))
print(odds)
odds = [n for n in nums if n % 2 != 0]
print(odds)

ages = (22, 15, 28, 18, 32, 19, 35)
teenagers = [age for age in ages if age >= 13 and age <= 19]
print(teenagers)

files = ["test5", "myvals", "test20", "builds"]
fnames = [s for s in files if s.startswith("test")]
print(fnames)

#####################################
#
#     $ filter.py
#     [3, 5, 7, 9]
#     [3, 5, 7, 9]
#     (15, 18, 19)
#     ['test5', 'test20']
#
