
carrito = []

def comprar_productos():

	productos = {1:['Botella con agua 50ml',5],2:['Pieza de pan 1',6],
             3:['Leche 1lt',23],4:['Pack 6u',25],5:['Mermelada 400gr',31],6:['Mayonesa 440gr',23],
             7:['Botella con agua 50ml',5],8:['Galletas 1u',37],
             }
	print("{:^1}{:^30}{:^5}".format('ID','PRODUCTO','P/U'))
	for codigo,producto in productos.items():
		print("{:^1}{:^30}{:^5}".format(codigo,(*producto)))

	i_producto,cantidad,salir = input("Ingresa el codigo del producto y cantidad y c/n>>").split(',')
	producto = productos.get(int(i_producto),'No existe el producto')
	precio_producto = producto[1]*(int(cantidad))
	print(f'Compraste {cantidad} unidades de {producto[0]}\tCosto: {precio_producto}')
	carrito.append([i_producto,producto[0],cantidad,precio_producto])


def ver_carrito():
	print("TU CARRITO DE COMPRAS ACTUAL\n")
	print("{:^1}{:^20}{:^10}{:^10}".format("ID","PRODUCTO","CANTIDAD","P/T"))
	for id_pro,producto,cantidad,precio in carrito:
		print("{:^1}{:^20}{:^10}{:^10}".format(id_pro,producto,cantidad,precio))


def pagar_carrito():

	pago_user = input("¿Desea realizar la compra? s/n>>").lower()
	if pago_user == 's':
		for producto in carrito:
			print(f'Debes pagar {sum(carrito[2])}')


def eliminar_carrito():

	del_prod = int(input("Ingresa el código de compra a eliminar>>"))
	carrito.pop(del_prod - 1)
	print(f'Se eliminó el producto')


def menu():
	opciones = ['Comprar productos','Ver carrito','eliminar_carrito','Pagar']
	for i,opcion in enumerate(opciones,start=1):
		print(i,opcion)

	opcion = int(input("Selecciona la opción>>"))
	if opcion:
		menu = {1:comprar_productos(),2:ver_carrito(),3:eliminar_carrito(),4:pagar_carrito()}
		return menu.get(opcion,'NO existe la opción')

print(menu())


