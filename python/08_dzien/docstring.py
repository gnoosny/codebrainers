def min(L):
	"""Funkcja szukajaca minimalnej wartosci

	Funkcja pobiera liste wartosci 
	i iteruje po nich zeby znalezc 
	najmniejsza
	
	>>> min([4,3,7,6,2])
	2

	>>> min([])
	Traceback (most recent call last):
  	File "<stdin>", line 1, in <module>
  	File "/home/dev/Desktop/szkolenie/python/08_dzien/docstring.py", line 6, in min
    najmniejsza1
	IndexError: list index out of range
	
	>>> min(None)
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	  File "/home/dev/Desktop/szkolenie/python/08_dzien/docstring.py", line 6, in min
	    najmniejsza1
	TypeError: 'NoneType' object is not subscriptable
	
	>>> min("Piotr")
	'P'
	>>> min([1, "P", 2+i])
	Traceback (most recent call last):
  	File "<stdin>", line 1, in <module>
	NameError: name 'i' is not defined
	
	>>> min(["pP", 2])
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	  File "/home/dev/Desktop/szkolenie/python/08_dzien/docstring.py", line 47, in min
	    if i < min_val:
	TypeError: '<' not supported between instances of 'int' and 'str'

	>>> min([2.33, 54.34, 1.21])
	1.21
	
	>>> min([-2, 435, -34, -55.4])
	-55.4
	
	>>> min([0])
	0

	>>> min([0])
	0

	"""
	min_val = L[0]
	for i in L:
		if i < min_val:
			min_val = i

	return min_val

if __name__ == "__main__":
	import doctest
	doctest.testmod()

# print(min.__doc__)

# help(min)

#print(help(min))