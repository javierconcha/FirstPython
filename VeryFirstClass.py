class MyClass:
    """A simple example class"""
    i = 12345
    def f(self):
        return 'Hello world. How are you?' 

class Complex:
	def __init__(self, realpart, imagpart):
		self.r = realpart
		self.i = imagpart

## MAIN
# -----------------------------------------------------------
x = MyClass()
print x.f()
print x.i +10000

y = Complex(2.0,-1.0)
print str(y.r) + '+' + str(y.i) + '*i'



# -----------------------------------------------------------