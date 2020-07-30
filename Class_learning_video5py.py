class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay): # self is an instance
        self.first = first
        self.last = last
        # self.email = f'{first}.{last}@company.com'
        self.pay = pay
        self.email = f'{self.first}.{self.last}@company.com'

    def fullname(self): # method
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)