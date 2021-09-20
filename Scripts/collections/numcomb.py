import itertools
import random
impares = [1,3,5,7,9]
for i in range(121):
	random.shuffle(impares)
	combinations = list(itertools.permutations(impares, 5))
	for c in combinations:
		print(sum(c))

