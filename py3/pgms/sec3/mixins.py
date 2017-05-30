#!/usr/bin/env python3
# mixins.py - Mixins

class Account(object):
    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance
    def deposit(self, amount):
        self.__balance += amount
    def withdraw(self, amount):
        self.__balance -= amount
    def inquiry(self):
        return self.__balance

class DepositCharge(object):
    def depositFee(self):
        self.withdraw(1.50)

class WithdrawCharge(object):
    def withdrawFee(self):
        self.withdraw(2.50)

class BrokerAccount(Account, DepositCharge, WithdrawCharge):
    def increase(self, amount):
        self.deposit(amount)
        self.depositFee()
    def decrease(self, amount):
        self.withdraw(amount)
        self.withdrawFee()

account = BrokerAccount("bob", 10000)
account.increase(100)      # 1.50
account.decrease(50)       # 2.50
print("$%-10.2f" %account.inquiry())

#################################################
#
#    $ mixins.py
#    $10046.00  
#
