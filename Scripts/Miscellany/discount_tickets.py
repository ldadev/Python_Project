from utility import *
"""
12)Realice un algoritmo que determine el pago a realizar por la entrada a un
espectaculo donde se pueden comprar solo hasta cuatro entradas, donde al costo 
de dos entradas se les descuenta el 10%, al de tres entradas el 15% y a la compra de
 cuatro tickets se le descuenta el 20 %.
"""

def show_discount():

    clear_screen()
    flag = True
    while flag:

        RATE = 1000
        print('-Ingrese el número de entradas ó enter para Salir\n')
        number_tickets = simple_int()

        if not number_tickets<=4:
            clear_screen()
            print('-Numero de entradas invalido.No se puede realizar el descuento\n')

        else:
            clear_screen()
            discount_tickets = {1:0,2:RATE*0.1,3:RATE*0.15,4:RATE*0.2}
            final_rate = RATE - discount_tickets[number_tickets]
            print(f'-La persona debe pagar {final_rate:,.0f} pesos ')

show_discount()







        
    

    
