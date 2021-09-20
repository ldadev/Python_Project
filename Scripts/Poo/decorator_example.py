from functools import wraps


def debug(f):
	@wraps(f)
	def new_function(*args):
		print(f"Function {f.__name__}() called!")
		return f(*args)
	return new_function

@debug
def add(*args):
	value = 0
	for n in args:
		value += n
	return value

@debug
def neg(*args):

	numbers = []
	for n in args:
		numbers.append(n * -1)
	return numbers

print(neg(3,4))