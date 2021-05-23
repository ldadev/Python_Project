class subset():

	def __init__(self,ln):

		ltemp = []
		self.ln = ln
		self.lf = []
		self.lf.append(ltemp)

		for n in ln:
			ltemp = [n]
			self.lf.append(ltemp)
			i = ln.index(n)
			i2 = 1
			while i + i2 < len(ln):
				ltemp.append(ln[i +i2])
				self.lf.append(ltemp)
				ltemp.pop()
				i2 +=1


	
	def __str__(self):
		return str(self.lf)

# {}, {1}, {2}, {1, 2}, {3}, {1, 3}, {2, 3}, {1, 2, 3}, {4}, {1, 4}
#, {2, 4}, {1, 2, 4}, {3, 4}, {1, 3, 4}, {2, 3, 4}, {1, 2, 3, 4}
n = subset([1,2,3,4])

set_1 = ['1','2','3','4']
subset= [[],[1,2,3,4],[1],[2],[3],[4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4],[1,2,3],[1,2,4],[1,3,4],[2,3,4]]

import copy

nums = [1,2,3,4]
subsets = [[]]

for n in nums:
    prev = copy.deepcopy(subsets)
    [k.append(n) for k in subsets]
    subsets.extend(prev)

print(subsets) 
print(len(subsets))

