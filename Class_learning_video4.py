#!/usr/bin/env python

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

# subclass that inherit Employee's attributes and methods
class Developer(Employee): 
    raise_amt =1.10
    
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay) # to inherit the first, last and pay handling from Employee class
        # Employee.__init__(self, first, last, pay) # also valid
        self.prog_lang =  prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay) # to inherit the first, last and pay handling from Employee class
        if employees == None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)  
            
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)  

    def print_emps(self):
        print('---------------')
        print(f'Employer: {self.fullname()}')
        for emp in self.employees:
            print('-->', emp.fullname())

dev_1 = Developer('Javier','Concha', 50000, 'Python')
dev_2 = Developer('Gustav','Pear', 60000, 'Java')

# list_employees = [dev1, dev2]
mgr_1 = Manager('Vitto','DeVito', 100000, [dev_1])

# print(isinstance(mgr_1,Employee))
# print(isinstance(mgr_1,Developer))
# print(isinstance(mgr_1,Manager))

print(issubclass(Developer,Employee))
print(issubclass(Manager,Employee))
print(issubclass(Manager,Developer))

# print(mgr_1.email)
# mgr_1.print_emps()
# mgr_1.add_emp(dev_2)
# mgr_1.print_emps()
# mgr_1.remove_emp(dev_1)
# mgr_1.print_emps()

# print(dev_1.email)
# print(dev_1.prog_lang)

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

# print(dev_1.email)
# print(dev_2.email)

# print(help(Developer))