let string = "";
let position = 1;
let tillTheEnd = 4;
for(let i = 0; i < 7; i++) {
	for(let j = 0; j < 8; j++) {
		if (i == 0 || i == 6){
			string += "*";
		}
		if (j == 0 && i!=0 && i !=6) {
			string += "*" + " ".repeat(position) + "*" + " ".repeat(tillTheEnd) + "*";
			tillTheEnd--;
			position++;
		}
		
		
	}
	string += "\n"
}

console.log(string);
