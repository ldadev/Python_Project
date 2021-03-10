from itertools import product


def calc():

	atomo = 'V','F'
	values_atom = []
	values_conj = []
	values_disj = []
	values_imp = []
	values_bic = []
	
	for c,d in product(atomo, repeat = 2):
		values_atom.append((c,d))

		if c == 'F' and d=='V' or c == 'F' and d == 'F' or c == 'V' and d == 'V':
			values_imp.append('V')
		else:
			values_imp.append('F')

		if c == 'V' and d=='V' or c == 'F' and d == 'F':
			values_bic.append('V')
	
		else:
			values_bic.append('F')
			values_conj.append('F')
			values_disj.append('V')

		if c == 'F' and d == 'F':
			values_conj.append('F')
			values_disj.append('F')
		elif c == 'V' and d == 'V':
			values_disj.append('V')
			values_conj.append('V')

	print('{:^5}{:^5}{:^5}{:^5}{:^5}'.format('p q','p^q','pvq','p>q','p<>q'),'\n')	
	for conjuncion,disjuncion,implicacion,bicon,atomo in zip(values_conj,values_disj,values_imp,values_bic,values_atom):
		print('{:^5}{:^5}{:^5}{:^5}{:^5}'.format(*atomo,conjuncion,disjuncion,implicacion,bicon))

calc()

