class Employee:

	def __init__(self, first, last, pay): # self is an instance
		self.first = first
		self.last = last
		self.pay = pay
		self.email = f'{first}.{last}@company.com'

	def fullname(self): # method
		return f'{first} {last}'

emp_1 = Employee('Javier','Concha', 50000)
emp_2 = Employee('Gustav','Pear', 60000)


print(emp_1.email)
print(emp_2.email)

pwd