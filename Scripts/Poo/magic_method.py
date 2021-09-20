from functools import wraps

def _int_required(f):
    @wraps(f)
    def wrapper(self, value):
        if not isinstance(value, int):
            raise TypeError("An integer is required.")
        return f(self, value)
    return wrapper

class Time:

	def __init__(self,h = 0,m = 0,s = 0):
		self.h = h
		self.m = m
		self.s = s

	@property
	def h(self):
		return self._h

	@h.setter
	@_int_required
	def h(self,value):
		self._h = value

a = Time('j',23,10)
print(a)

