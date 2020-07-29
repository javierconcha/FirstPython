class Employee:

	num_of_emp = 0
	raise_amount = 1.04 # class variable

	def __init__(self, first, last, pay): # self is an instance
		self.first = first
		self.last = last
		self.pay = pay
		self.email = f'{first}.{last}@company.com'

		Employee.num_of_emp += 1

	def fullname(self): # regular method
		return f'{first} {last}'

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)	



emp_1 = Employee('Javier','Concha', 50000)
emp_2 = Employee('Gustav','Pear', 60000)
emp_1.raise_amount = 1.05
emp_1.apply_raise()

emp_3 = Employee('Marilena','Roma', 50000)

print(Employee.raise_amount)
print(emp_1.pay)
print(emp_2.pay)

print(Employee.num_of_emp)
print(emp_1.num_of_emp)
