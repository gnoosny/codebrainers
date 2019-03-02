#a to kanapa pana kota

palindrom = input("wpisz tekst, ktory chcesz sprawdzic: ")
#print()

#palindrom = 'a to kanapa pana kota'
print("tekst poczatkowy: " + palindrom)

palindrom = palindrom.replace(" ", "")


print("tekst bez spacji: " + palindrom)
palindrom2 = ""

for i in palindrom:
	palindrom2 = i + palindrom2
	
print("odwrocony tekst: " + palindrom2)

if palindrom == palindrom2:
	print("tak to jest palindrom")
else:
	print("to nie jest palindrom")
	
inny sposob:	
# if tekst == tekst[::-1]:
# print("jest palindromem")
