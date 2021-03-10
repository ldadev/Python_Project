def primo(n):
    esprimo=True
    for c in range (2,int(n/2)+2)
        if n % c==0:
            esprimo=False
            break
    return esprimo
numeros=int(input("Ingrese un numero:"))
list_primos=[]
divisores=[]
for i in range(1,numeros+1):
    if primo(i)==True:
        list_primos.append(i)
print('Primos:{0}'.format(list_primos))
