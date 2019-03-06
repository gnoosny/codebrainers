#m = input("wypisz m: ")
#m = int(m)




def fibonacci(m):
	if not isinstance(m, int):
		raise Exception("to nie jest int")
	if m < 2:
		raise Exception("liczba musi byc wieksza niz 1")
	list = [0, 1]
	for i in range(2, m+1):
		list.append(list[i-1] + list[i-2])
	return list[m], list

try:
	print(fibonacci(1))

except Exception as exc:
	print(exc.args)
	
