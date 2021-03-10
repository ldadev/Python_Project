"""
import numpy as np

grid = [[0,3,4,0,0,9,5,7,0],
[0,0,0,0,0,0,0,0,0],
[7,0,0,0,0,0,0,0,0],
[0,0,0,0,8,7,0,2,0],
[0,4,0,0,0,0,0,3,0],
[0,8,0,5,0,0,7,1,0],
[4,0,1,0,0,2,6,0,0],
[0,0,2,9,0,0,0,5,3],
[9,0,0,0,0,0,0,0,1]]

def possible(x,y,n):

	for i in range(0,9):
		if grid[y][i] == n:
			return False

	for i in range(0,9):
		if grid[i][x] == n:
			return False

	x0=(x//3)*3
	y0=(y//3)*3
	for i in range(0,3):
	    for j in range(0,3):
	    	if grid[y0 + i][x0 + j] == n:
	    		return False
	    return True

		

def solve():
	global grid
	for y in range(9):
		for x in range(9):
			if grid[y][x] == 0:
				for n in range(1,10):
					if possible(y,x,n):
						grid[y][x] = n
						solve()
						grid[y][x] = 0
				return
	print(np.matrix(grid))
	input('Solve?')	
solve()


"""

import numpy as np

grid = ['X',' ','X','X',' ','X','X',' ','X']


def ganador(letra):
	if grid[0] == letra and grid[1] == letra and grid[2]==letra or grid[3] == letra and grid[4] == letra and grid[5] == letra or grid[6] == letra and grid[7] == letra and grid[8] == letra:
	    return True


copia = grid

def posibles():

	for i in range(9):
		grid[i] = 'X'
		if ganador('X'):
			print(i)
		
			

posibles()

print(grid)
"""
def jugada_pc(x,n):

	for i in range(1,10):
		if grid[x] == n:
			return False
		
		if ganador('X'):
			if True:
			grid[x] = 'O'

jugada_pc(2,'X')

print(np.matrix(grid))

"""