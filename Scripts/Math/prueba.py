
nums = input("Enter: ")
a = 0
b = 0
nums_list = []
flag = False
if nums[0] == "-":
	nums = nums[1:]#La lista se porciona desde el indice 1
	flag = True
for i in range(len(nums)):
	if nums[i] == "+" or nums[i] == "-":
		b = i  #el indice posterior
		nums_list.append(nums[a:b])#porcion con signo y numero
		a = i #EL indice anterior
if flag:
	nums_list[0] = '-' + nums_list[0] #Si el número inicio con signo positivo se agrega un signo - al primer número

nums_list.append(nums[b:])#se ingresa el slice del ultimo numero con su signo
count = sum([int(ent) for ent in nums_list])

print(count)
