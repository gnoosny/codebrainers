import random
number = random.randrange(0, 101, 1)

print(number)



guesed = False
tries = 0

while (not guesed) and (tries < 7):
	g = input("podaj jakas liczbe pomiedzy 0 a 100: ")
	g = int(g)
	if g > number:
 		print("the number that I choosed is smaller")
 		tries += 1
	elif g < number:
 		print("the number that I choosed is bigger")
 		tries += 1
	elif g == number:
 		print("You've guesed it, the number I choosed is " + str(number))
 		guesed = True

 		
 		## zgadles w x probie
 		## przegrales