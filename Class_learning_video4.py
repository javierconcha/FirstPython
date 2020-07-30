#!/usr/bin/env python

class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay): # self is an instance
        self.first = first
        self.last = last
        # self.email = f'{first}.{last}@company.com'
        self.pay = pay
        self.email = f'{first}.{last}'

    # def fullname(self): # method
    #     return f'{first} {last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

# subclass that inherit Employee's attributes and methods
class Developer(Employee): 
    pass

dev_1 = Developer('Javier','Concha', 50000)
dev_2 = Developer('Gustav','Pear', 60000)



# print(dev_1.email)
# print(dev_2.email)

# print(help(Developer))