for i in range(0,101):
	if i%3 == 0 and i%5 !=0 and i%15 !=0:
		print(str(i) + ' Fizz')
	if i%5 == 0 and i%15 !=0:
		print(str(i) + ' Buzz')
	if i%15 == 0:
		print(str(i) + ' FizzBuzz')