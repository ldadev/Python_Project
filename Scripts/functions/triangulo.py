
print()
def diamond(width):

	for i in list(range(1,width)) + list(range(width,0,-1)):
		print(' ' + (width - i) * ' ' + i * ('* '))

diamond(15)
print()

