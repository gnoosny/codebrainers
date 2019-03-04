a = input("podaj a: ")
b = input("podaj b: ")
c = input("podaj c: ")
a = float(a)
b = float(b)
c = float(c)

def deltah(a, b, c):
	delt = b**2 - 4 * a * c
	print("delta: " + str(delt))
	if delt > 0:
		x1 = (-b-(delt**0.5))/2*a
		x2 = (-b+(delt**0.5))/2*a
		return x1, x2
	if delt == 0:
		x1 = -b/(2*a)
		return x1
	if delt < 0:
		return False
		
	
print(deltah(a, b, c))