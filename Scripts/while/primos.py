import math

for n in range(1,20,2):
	if n % 3 == 0:
		continue
		pass




primos = []
def mostrar_primo(numero):

	es_primo = True

	for i in range(2,numero,1):
		if numero%i == 0:
			es_primo = False
			break

	if es_primo:
		primos.append(numero)

for i in range(1,100):
	mostrar_primo(i)

print(primos)

# Teorema de fermat
primo = [i for i in range(1,100) if 2**(i-1) % i == 1]


# Criba de eratostenes

print('Criba de eratostenes\n')
numeros = list(range(1,100))
for index,value in enumerate(numeros,1):
	for n in range(1,value):
		m = value*n
		if m < len(numeros) and m == value:
			numeros.remove(m)
print(numeros)
