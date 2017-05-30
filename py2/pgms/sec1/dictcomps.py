#!/usr/bin/env python
# dictcomps.py - dictionary comprehensions

D1 = {"ACME" : 45.23, "AAPL" : 94.43, "IBM" : 192.05,
          "HPQ" : 34.81, "FB" : 68.42}

# create dictionary with lower case stock names
D2 = {name.lower() : price for (name, price) in D1.items()}
print D2

# create dictionary with stock prices over $50
D3 = { 
    name : price for (name, price) in D1.items() if price > 50.00
}
print D3

#####################################
#
#    $ dictcomps.py
#    {'acme': 45.23, 'hpq': 34.81, 'fb': 68.42, 'aapl': 94.43, 'ibm': 192.05}
#    {'FB': 68.42, 'AAPL': 94.43, 'IBM': 192.05}
#      
