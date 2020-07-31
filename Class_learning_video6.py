class Employee:

    raise_amt = 1.04

    def __init__(self, first, last): # special methods. Magic method. Dunder init
        self.first = first
        self.last = last

    @property
    def email(self): # method
        return f'{self.first}.{self.last}@email.com'

    @property
    def fullname(self): # method
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete name!')
        self.first = None
        self.last = None

emp_1 = Employee('Javier','Concha') 

# property decorator
# property decorators allow to define a method but access it as an attribute
emp_1.fullname = 'Gustav Pear'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)