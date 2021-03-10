

hexa = '181A1D8028292C80448015803B2D2680'

new_hex = ''

for i in range(1,len(hexa),8):

	new_hex+= hexa[i - 1:i + 5]

print(new_hex)