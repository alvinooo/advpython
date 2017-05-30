#!/usr/bin/env python3
# diamond.py - Diamond inheritance

class Machine(object):
    def __init__(self):
        print("Machine constr")

class Fax(Machine):
    def __init__(self):
        super().__init__()
        print("Fax constr")

class Copier(Machine):
    def __init__(self):
        super().__init__()
        print("Copier constr")

class CopierFax(Copier, Fax):
    def __init__(self):
        super().__init__()
        print("CopierFax constr")

copyier = CopierFax()

#################################################
#
#    $ diamond.py
#    Machine constr
#    Fax constr
#    Copier constr
#    CopierFax constr
#
