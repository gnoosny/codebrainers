import random
number = random.randrange(0, 101, 1)

# print(number)


guesed = False
tries = 0

while (not guesed) and (tries < 7):
	try:
		g = input("podaj jakas liczbe pomiedzy 0 a 100: ")
		g = int(g)
	except KeyboardInterrupt:
		print("\n\nBaby come back! <3")
		break

	if tries == 6:
 		print("You didn't guesed it")
 		break
	elif g > number:
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