class Parent:

	def __init__(self, eye_color="", length=0,last_parent=""):
		self.eye_color = eye_color
		self.length = length
		self.last_parent = last_parent

class Child(Parent):

	def __init__(self,*args, **kwargs):
		super().__init__(*args, **kwargs)

x = Parent("Blue", 2)
y = Child("Black",4)


def date():
	objects = Parent()
	print(x.eye_color)

date()

print(x.length, x.eye_color)
print(y.length, x.eye_color)

