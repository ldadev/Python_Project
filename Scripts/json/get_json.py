import json

with open('data.json') as file:
	data = json.load(file)
	
	for name,price in data.items():
		print(name,price)


