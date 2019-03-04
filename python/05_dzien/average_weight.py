def average_w(list_, list_weight):
	sum = zip(list_, list_weight)
	#print(sum)
	licznik = 0
	mianownik = 0
	for i, j in sum:
		licznik += i * j
		mianownik += j
	return licznik/mianownik
		
list_ = [1, 2, 3]
list_weight = [1, 4, 2]
print(average_w(list_, list_weight))


	