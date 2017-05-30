#!/usr/bin/env python3
# lambdadict.py - lambdas with dictionaries

coins = { "pennies" : 8, "nickles" : 3, 
          "dimes" : 5, "quarters" : 2 }

for (name, amount) in sorted(list(coins.items()),
        key = lambda k_v : (k_v[1],k_v[0])):
        #key = lambda(k,v) : (v,k), reverse=True):
   print(name, amount)

#####################################
#
#     $ lambdadict.py
#     quarters 2
#     nickles 3
#     dimes 5
#     pennies 8
#      
