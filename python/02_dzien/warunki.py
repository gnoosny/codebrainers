liczba1 = 4
ulamek1 = 0.3
lista1 = ['kot', 'pies', 'zyrafa', 'slon', 'lew']
tekst1 = "To jest przykladowy tekst"
logika1 = True
none1 = None 

liczba2 = 48
ulamek2 = 0.436457
lista2 = ['ford', 'kia', 'porsche', 'ferrari', 'polonez']
tekst2 = "To jest drugi przykladowy tekst"
logika2 = False
none2 = None

print(liczba1)
print(ulamek1)
print(lista1)
print(tekst1)
print(logika1)
print(none1)

print(liczba2)
print(ulamek2)
print(lista2)
print(tekst2)
print(logika2)
print(none2)

# to jest komentarz w pythonie, wielolinijkowych komentarzy nie ma
print('\n')

if none1 == none2: print("tak nony sa rowne")
print('\n')

if liczba1 == liczba2:
	print('tak liczba1 i liczba2 sa rowne')
elif ulamek1 <= ulamek2:
	print('ulamek1 jest mniejszy od ulamka2 i wynosi', ulamek1)
	
print('\n')

if liczba1 == liczba2:
	print('tak liczba1 i liczba2 sa rowne')
elif ulamek1 >= ulamek2:
	print('ulamek1 jest mniejszy od ulamka2')
else:
	print('tu nic nie ma sensu')