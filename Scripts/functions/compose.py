import math

def P(x):

	p = 2*x + 1
	return p


def A(x):

	a = 3**x
	return a


def N(x):
	n = math.sqrt(5*x + 4)
	return n


w = int(input())

for z in range(w):
	print(P(A(N(z))))