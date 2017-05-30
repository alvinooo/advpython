#!/usr/bin/env python
# filter.py - filter function

def oddNum(n):
    return n % 2 != 0

nums = [2, 3, 4, 5, 6, 7, 8, 9]
odds = filter(oddNum, nums)
print odds
odds = filter(lambda n : n % 2 != 0, nums)
print odds

ages = (22, 15, 28, 18, 32, 19, 35)
teenagers = filter(lambda age : age >= 13 and age <= 19, ages)
print teenagers

files = ["test5", "myvals", "test20", "builds"]
fnames = filter(lambda s : s.startswith("test"), files)
print fnames

#####################################
#
#     $ filter.py
#     [3, 5, 7, 9]
#     [3, 5, 7, 9]
#     (15, 18, 19)
#     ['test5', 'test20']
#
