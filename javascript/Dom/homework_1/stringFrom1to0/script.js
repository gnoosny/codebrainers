let string = "";
for (let i = 0; i < 10; i++) {
	string += i
}
string = string.substring(1,10) + string.substring(0,1);

console.log(string)
