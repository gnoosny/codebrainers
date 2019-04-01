import csv

with open('przykladowy.csv', 'r') as f:
	czytacz = csv.reader(f)
	for wiersz in czytacz:
		#w = int(wiersz[1])
		#if  wiersz[1] < 10:
			print(wiersz)