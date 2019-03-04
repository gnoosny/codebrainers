a = input("podaj a: ")
b = input("podaj b: ")
a = float(a)
b = float(b)

def pit(a, b):
	c = (a**2 + b**2)**(1/2)
	return c
	
print(pit(a,b))