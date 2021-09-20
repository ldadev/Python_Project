
"""
def user_input():

	flag = True
	while flag:
		try:
			number_row = int(input('Enter the number of rows>>')) - 1
			if number_row > 0:
				return number_row
			else:
			    print(f'Only positive numbers greater than 0.')	
		except Exception as e:
			print(f'Invalid entry. The error has occurred {e}.')
	

user_entry = user_input()
all_rows = [[1],[1,1]]

row_index = 0

while row_index < user_entry:
	row_index+=1
	new_row = [1]

	for i in range(len(all_rows[row_index]) - 1):
		new_row+=[all_rows[row_index][i] 
		       + all_rows[row_index][i + 1]]
	new_row+=[1]
	all_rows.append(new_row)


size_all_rows = len(all_rows)
for i in range(len(all_rows)):
	print((size_all_rows-i)*'  ' + str(all_rows[i]))

"""








def user_input():

	flag = True
	while flag:
		try:
			number_row = int(input('Enter the number of rows>>')) - 1
			if number_row > 0:
				return number_row
			else:
			    print(f'Only positive numbers greater than 0.')	
		except Exception as e:
			print(f'Invalid entry. The error has occurred --> {e}.')
	

def show_triangule():

	user_entry = user_input()
	all_rows = [[1],[1,1]]

	row_index = 0

	while row_index < user_entry:
		row_index+=1
		
		new_row = [1] + list(map(lambda i:all_rows[row_index][i] 
			      + all_rows[row_index][i + 1],range(len(all_rows) - 1))) + [1]
		all_rows.append(new_row)
		
	size_all_rows = len(all_rows)
	for i in range(len(all_rows)):
		print((size_all_rows-i)*'  ' + str(all_rows[i]))

	with open('' + 'pascal_triangule.txt','w') as file:
		file.writelines(str(all_rows))



if __name__ == '__main__':
	show_triangule()






