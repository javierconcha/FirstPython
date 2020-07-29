class Employee:

	num_of_emp = 0
	raise_amt = 1.04 # class variable

	def __init__(self, first, last, pay): # self is an instance.
		self.first = first
		self.last = last
		self.pay = pay
		self.email = f'{first}.{last}@company.com'

		Employee.num_of_emp += 1

	def fullname(self): # regular method that takes instance as first argument
		return f'{first} {last}'

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amt)	

	@classmethod # decorator
	def set_raise_amt(cls, amount):
		cls.raise_amt = amount

	# constructor	
	@classmethod
	def from_string(cls, emp_str):
		first, last, pay = emp_str.split('-')
		return cls(first, last, pay)

	@staticmethod
	def is_workday(day):
		if day.weekday() == 5 or day.weekday() == 6:
			return False
		return True


emp_1 = Employee('Javier','Concha', 50000)
emp_2 = Employee('Gustav','Pear', 60000)



# Third video
# https://youtu.be/rq8cL2XMM5M
# Employee.set_raise_amt(1.05)

# print(Employee.raise_amt)
# print(emp_1.raise_amt)
# print(emp_2.raise_amt)

# emp_str_1 = 'Javier-Concha-50000'
# new_emp_1 = Employee.from_string(emp_str_1)

# print(new_emp_1.email)
# print(new_emp_1.pay)

# import datetime
# my_date = datetime.date(2016, 7, 11)

# print(Employee.is_workday(my_date))

# Second video
# print(emp_1.__dict__)
# emp_1.raise_amt = 1.05
# emp_1.apply_raise()
# print(Employee.__dict__)
# print(emp_1.__dict__)

# emp_3 = Employee('Marilena','Roma', 50000)

# print(Employee.raise_amt)
# print(emp_1.pay)
# print(emp_2.pay)

# print(Employee.num_of_emp)
# print(emp_1.num_of_emp)
