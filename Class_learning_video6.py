class Employee:

    raise_amt = 1.04

    def __init__(self, first, last): # special methods. Magic method. Dunder init
        self.first = first
        self.last = last
        self.email = f'{self.first}.{self.last}@company.com'

    def fullname(self): # method
        return f'{self.first} {self.last}'

emp_1 = Employee('Javier','Concha', 50000) 
emp_2 = Employee('Gustav','Pear', 60000)