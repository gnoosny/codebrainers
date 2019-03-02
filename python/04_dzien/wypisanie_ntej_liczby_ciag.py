m = input("wypisz m: ")
m = int(m)
list = [0, 1]

# 0 1 1

for i in range(2, m+1):
	list.append(list[i-1] + list[i-2])
	
print(list)
print("\n")	
print(str(m) + " wyraz ciagu to " + str(list[m]))
	