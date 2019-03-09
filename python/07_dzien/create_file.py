text = input("enter text: ")
name = input("enter name of file: ")

with open(name, 'w') as f:
	f.write(text + '\n')