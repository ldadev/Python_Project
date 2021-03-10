

sales = {'A':500,'B':260,'C':240}

max_sale = max(sales.values())
min_sale = min(sales.values())

def item_a():

	print('ITEM A')
	for seller,sale in sales.items():
		if sale == max(sales.values()):
			return f'Las ventas mas elevandas son del vendedor {seller} con {sale} ventas'

print(item_a())

def item_b():

	print('ITEM B')
	print('{:^1}{:^10}'.format('VENDEDOR','VENTAS'))
	for seller,sale in sales.items():

		if sale > 200:
			print('{:^10}{:^6}'.format(seller,sale))

item_b()

def item_c():

	print('ITEM C')
	print('{:^1}{:^10}'.format('VENDEDOR','VENTAS'))
	for seller,sale in sales.items():

		if sale > 400:
			print('{:^10}{:^6}'.format(seller,sale))
item_c()

def item_e():

	print('ITEM E')
	print('{:^1}{:^10}'.format('VENDEDOR','VENTAS'))
	for seller,sale in sales.items():

		if sale <max_sale and sale > min_sale:
			return '{:^10}{:^6}'.format(seller,sale)

print(item_e())

def item_f():

	print('ITEM F')
	return 'El total de ventas esta entre {} y {}'.format(min_sale,sum(sales.values()))

print(item_f())