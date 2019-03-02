text = "Ala ma kota, a kot ma Alę"
text = text.replace(" ","").lower().replace(",","")
print(text)

dict = {
	"a": 0,
	"l": 0,
	"m": 0,
	"k": 0,
	"t": 0,
	"o": 0,
	"ę": 0
}

for i in text:
	if i == 'a':
		dict["a"] += 1
	if i == 'l':
		dict["l"] += 1
	if i == 'm':
		dict["m"] += 1
	if i == 'k':
		dict["k"] += 1
	if i == 't':
		dict["t"] += 1
	if i == 'o':
		dict["o"] += 1
	if i == 'ę':
		dict['ę'] += 1
		
print(dict)

dict2 = {}
for i in text:
	if i in dict2:
		dict2[i] += 1
	else:
		dict2[i] = 1
print(dict2)