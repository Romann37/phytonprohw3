#Написать итератор, который принимает список списков, и возвращает их плоское представление. 

class FlatIterator:
	def __init__(self, x: list):
		self.x = x

	def __iter__(self):
		self.count = -1
		return self

	def __next__(self):
		self.count += 1
		if self.count == len(self.x):
			raise StopIteration
		mylist = '\n'.join(self.x[self.count])
		return mylist


nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	['g', 'h', 'i']
]
for item in FlatIterator(nested_list):
	print(item)
