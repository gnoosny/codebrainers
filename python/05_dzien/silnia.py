zasieg = input("podaj zakres: ")
zasieg = int(zasieg)

def silnia(n):
	sum = 1
	for i in range(2, n+1):
		sum *= i
		#print(sum)
	return sum
	
print(silnia(zasieg))
