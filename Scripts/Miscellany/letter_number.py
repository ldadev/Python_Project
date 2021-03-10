
from utility import*

"""11) Desarrolle un algoritmo que permita convertir un valor numerico 
dado a un valor en letras, segun la siguiente tabla:
A = 19 y 20, B =16, 17 y 18, C = 13, 14 y 15, D = 10, 11 y 12, E = 1 hasta el 9. 
Se asume que la nota esta comprendida entre 1 y 20.
"""

def relation_number():

    clear_screen()
    flag = True
    while flag:
        print('Ingresa un número del 1 al 20. Para encontrar su letra ó enter:Salir')
        number = simple_int()

        if not 1<=number<=20:
            print('Número fuera del rango. Intentalo de nuevo')
            continue

        relation = {'E':range(1,10),'D':range(10,13),'C':range(13,16),'B':range(16,19),'A':range(19,21)}

        for key,value in relation.items():
            if number in value:
                print(f'Al número {number} le pertenece la letra {key}')         
        flag = False    

relation_number()








