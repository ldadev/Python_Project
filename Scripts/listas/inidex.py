
data_origin = [[1,2,7],[2,4,11],[0,3,12]]

def search():

	data_new = []

	for array in data_origin:
		try:
			if array[2] >= 7:
				data_new.append(array)
		except:
			return f'No existe el indice 2 en la lista {array}\nResultado : {data_new}'
	return data_new
print(search())
