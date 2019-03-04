# your code goes here
text = input("wpisz tekst: ")
#text = "jakis tekst"

def dictionary(text):
	#text = text.replace(" ","").lower().replace(",","").replace(".","")
	text = text.replace("\W","").lower()
	dict = {}
	for i in text:
		if i in dict:
			dict[i] += 1
		else:
			dict[i] = 1
	return dict
	
print(dictionary(text))

