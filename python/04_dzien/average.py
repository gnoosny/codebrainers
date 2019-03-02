list = [1, 5, 3, 77, 35, 345, 5.435, 354.3, 566, 43.3]
weight = [1, 1, 1, 3, 4, 5, 1, 4, 3, 4]
sum = []
avg = 0
avg_weight = 0
avg_geo = 1

#for i in list:
#		sum.append(i*float(weight))
		
#print(sum)

for i in list:
	avg += i
print("lista wartosci: " + str(list))
print("srednia arytmetyczna: " + str(avg/len(list)) + "\n")

print("lista wag: " +str(weight))
sum = zip(list, weight)

for i, x in sum:
	avg_weight += i*x

print("srednia wazona: " + str(avg_weight/len(list)) + "\n")
#list(zip(list,weight)

for i in list:
	avg_geo *= i

avg_geo = avg_geo*(1/len(list))

print("srednia geometryczna: " + str(avg_geo))


