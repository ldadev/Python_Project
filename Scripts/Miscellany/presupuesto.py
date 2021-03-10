
food = {
	'Rice':2000,
	'potatos':1520,
	'spagheti':2000,
	'orange':1523
       }


presupuesto = int(input('Ingrese su presupuesto para la compra>>'))
total_costo = sum(food.values()) - presupuesto# abs--> total_costo simpre sera positivo

msg = 'Le sobran' if total_costo < presupuesto else 'Le faltan'
print(f'{msg} $ {abs(total_costo)}')

