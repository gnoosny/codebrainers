a = 777;
b = 24;
c = 325;

biggestNum = [];

biggestNum.push(a);
biggestNum.push(b);
biggestNum.push(c);
biggest = biggestNum[0];

for(let i = 0; i < biggestNum.length; i++) {
	if (biggestNum[i] > biggest) {
		biggest = biggestNum[i];
	}
}

console.log(biggestNum);
console.log(biggest);
