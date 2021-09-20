array = [123,456,789,1,544,20,500,999]

for index,num in enumerate(array):
	data = list(map(lambda x,y:(((x,y),num + x == 1000),
		    ((x,y),num + y == 1000)),array[index + 1:],array[:index + 1]))
	
