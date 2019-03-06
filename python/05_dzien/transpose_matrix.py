list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list2 = [[0, 1, 2], [1, 2, 2]]

def transpose(arr):
	return [*zip(*arr)]
	
print(transpose(list))
print(transpose(list2))