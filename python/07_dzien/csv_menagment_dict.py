import csv
import statistics

with open('przykladowy.csv', 'r') as f:
	czytacz = csv.DictReader(f)
	list_score = []
	list_year = []
	for wiersz in czytacz:
		score = int(wiersz["Score"])
		year = int(wiersz["Year"])
		search_score = 50
		search_year = 0
		#linia = []
		#linia += score, year
		list_score.append(score)
		list_year.append(year)
		if  score < search_score:
			#print(wiersz["Title"])
			pass

		#print(linia)

#print("lista ocen:\n", list_score, "\n")
#print("lista lat:\n", list_year, "\n")
movies = zip(list_year, list_score)
avg = 0
j_len = len(list_score)

min_score = 100
max_score = 0
year_min = 0
year_max = 0

for i, j in movies:
 	avg += j
 	if min_score > j:
 		min_score = j
 		year_min = i
 	if max_score < j:
 		max_score = j
 		year_max = i

avg = avg/j_len
print("srednia: " + str(avg))
print("najnizsza_wartosc: " + str(min_score) + " w roku: " + str(year_min))
print("najwyzsza wartosc: " + str(max_score) + " w roku: " +str(year_max))
sorted_score = sorted(list_score)
len_sorted_score = len(sorted_score)
#print(len_sorted_score)
len_sorted_score = 80

if len_sorted_score % 2 != 0:
	i = int(len_sorted_score/2)
	print(i)
	print("Mediana: " + str(sorted_score[i]))
elif len_sorted_score % 2 == 0:
	i = int(len_sorted_score/2)
	print("i", i)
	avg_i = int((sorted_score[i] + sorted_score[i+1])/2)
	print(avg_i)
	print("Mediana: " + str(sorted_score[avg_i]))
#print(sorted_score)

std_deviation = 0

for i in sorted_score:
	std_deviation += (i - avg) ** 2
	std_deviation /= len(sorted_score)
print("wariancja to: ", std_deviation)

std_deviation**=0.5
std_deviation = std_deviation/len(sorted_score)
print("odchylenie standardowe to: ", std_deviation)

#dev = stdev(sorted_score)
#print(dev)
