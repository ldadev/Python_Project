
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

porciones = 0
for i in range(1,4):
	porciones+=10
	print(primos[porciones-10:porciones])