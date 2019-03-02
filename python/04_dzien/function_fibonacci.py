m = input("wypisz m: ")
m = int(m)

def fibonacci(m):
	list = [0, 1]
	for i in range(2, m+1):
		list.append(list[i-1] + list[i-2])
	return list[m], list

wartosc = fibonacci(m)

print(wartosc)