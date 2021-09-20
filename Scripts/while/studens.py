
people = []
n = 0
while n < 10:
	n+=1
	people.append(input('Ingrese la persona>>'))

count_people = dict(map(lambda x: (x,people.count(x)),people))
