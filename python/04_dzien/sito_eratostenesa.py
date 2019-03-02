sito = [True] * 100
#lista jednoelementowa razy sto daje liste stuelementowa

sito[0] = False
sito[1] = False

for i in range(2, 51):
	n = 2
	wielokrotnosc = i * n
	while wielokrotnosc < 100:
		sito[wielokrotnosc] = False
		n += 1
		wielokrotnosc = n * i
		
for indeks, wartosc in enumerate(sito):
	if wartosc:
		print("Liczba pierwsza: ", indeks)