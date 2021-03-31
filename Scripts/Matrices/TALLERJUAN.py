import math

"""
opcion = 0
def menu():
    opc = int(input("Menu Principal \n" +
                    "1. Numero a potencia \n" +
                    "2. Si tiene raiz \n" +
                    "3. isosceles,equilatero,escaleno \n" +
                    "4. Matriz \n" +
                    "5. Mayor elemento \n" +
                    "6. Elemento que mas se repite  \n" +
                    "7. Diagonal segundaria  \n" +
                    "8. Suma de valores en la periferia  \n" +
                    "9. Salir  \n" +
                    "Elija una Opcion : \n"))

    return opc
#funcion numeor a potencia
def pot(a,b):
     resultado=1
     for i in range(b):
        resultado*=a
     return resultado
#funcion ecuacion
def ecuacioncuadratica( a, b, c):
    dis = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(dis))
    if dis > 0:
        print((-b + sqrt_val)/(2 * a))
        print((-b - sqrt_val)/(2 * a))
    elif dis == 0:
        print(-b / (2 * a))
    else:
        print(- b / (2 * a), " + i", sqrt_val)
        print(- b / (2 * a), " - i", sqrt_val)
#funcion triangulo
def tip_triangulo(a,b,c):
    if a==b==c:
        print('equilatero')
    elif a==b or b==c or c==a:
        print('isoseles')
    else:
        print('escaleno')

#funcion matriz
def matriz(m,n):
    return[[i*j for j in range(n)] for i in range(m)]
#mayor elemnto de una matriz
def BuscarMayor(Cantidad):
    Cantidad=Cantidad-1
    Numero=int(input())
    Numero2=Numero
    if Cantidad>0 :Numero2=BuscarMayor(Cantidad)
    if Numero2>Numero:
       return Numero2
    else:
       return Numero
# funcion elemento que mas se repite
def num_rep(arr):
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if(arr[i] == arr[j]):
                print(arr[j]);
# diagonal segundaria

# suma valor periferia

while opcion != 9:
    opcion = menu()
    if opcion == 1:
        a=float(input("ingresar base: \n"))
        b=float(input("ingresar exponente: \n"))
        print(math.pow(a,b))
    if opcion == 2:
        a=float(input())
        b=float(input())
        c=float(input())
        if a == 0:
            print("ingrese ecuacion validad")
        else:
            ecuacioncuadratica(a, b, c)
    if opcion == 3:
        a = int(input())
        b = int(input())
        c = int(input())
        tip_triangulo(a,b,c)
    if opcion == 4:
        filas=int(input())
        columnas=int(input())
        matriz=matriz(filas,columnas)
        print(matriz)
    if opcion == 5:
        Cantidad=int(input("Cuantos Numeros: "))
        print ("El mayor es",BuscarMayor(Cantidad))
    if opcion == 6:
        arr = [1,1,2,3,4,5]
        num_rep(arr)
    #if opcion == 7:
    #if opcion == 8:
    if opcion == 9:
        print("Programa terminado")

    if opcion > 9:
        print("opcion invalida")
"""



def repeat_items(matriz):

	items = []
	for row in matriz:
		items+=row# Descomprimimos los elementos de cada fila de la matriz

	columns_item = [(row.index(item),item) for row in matriz for item in row]# Guardamos en tuplas (columna,elemento)
	conteo = {item:(index,items.count(item)) for index,item in columns_item}# contamos y guardamos en un diccionario
	print(conteo)

repeat_items( [['leche','pan','queso'],['azucar','pan','huevos'],['arroz','pan','pollo']])

