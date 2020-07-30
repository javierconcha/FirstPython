class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay): # special methods. Magic method. Dunder init
        self.first = first
        self.last = last
        # self.email = f'{first}.{last}@company.com'
        self.pay = pay
        self.email = f'{self.first}.{self.last}@company.com'

    def fullname(self): # method
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)   

    # Special methods
    def __repr__(self): # return a string to recreate an object
        return f'Employee({self.first}, {self.last}, {self.pay})'

    def __str__(self):
        return f'{self.fullname()} - {self.email}'  

    def __add__(self, other):
        return self.pay + other.pay 

    def __len__(self):
        return len(self.fullname())        

emp_1 = Employee('Javier','Concha', 50000) 
emp_2 = Employee('Gustav','Pear', 60000)

# special methods: https://docs.python.org/3/reference/datamodel.html#special-method-names

# print(len(emp_1))

# print(len('test'))
# print('test'.__len__())

# add "add" special method
# print(emp_1+emp_2)

# print(1+2)
# print(int.__add__(1, 2))
# print('a' + 'b')
# print(str.__add__('a', 'b'))

# print(emp_1) without __repr__: <__main__.Employee object at 0x10c328250>

# print(emp_1) # with __repr__: Employee(Javier, Concha, 50000)
# print(emp_1) # with __str__:Javier Concha - Javier.Concha@company.com

# print(repr(emp_1))
# print(str(emp_1))

# print(emp_1.__repr__())
# print(emp_1.__str__())
