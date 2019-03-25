let a = 7;
let b = 10;
let c = 15;

let biggestNumber = [];
biggestNumber.push(a);
biggestNumber.push(b);
biggestNumber.push(c);

biggest = biggestNumber[0];

for (let i = 1; i < biggestNumber.length; i++) {
    if (biggestNumber[i] > biggest) {
        biggest = biggestNumber[i];
    }
}

console.log(biggest);

if (Math.pow(a, 2) + Math.pow(b, 2) == Math.pow(c, 2)) {
    console.log('Trójkąt jest prostokątny')
} else {
    console.log('Trójkąt nie jest prostokątny')
}
let tmp = "";
let size = 8
for (let i = 0; i < size; ++i) {
    tmp = " "
    for (let j = 0; j < size; ++j) {
        if (i == 0 || i == (size - 1)) {
            tmp += "*";
        }
        else {
            if (j == 0 || j == (size - 1)) {
                tmp += "*";
            }
            else if (j == i) {
                tmp += "*";
            }
            else {
                tmp += " "
            }
        }
    }
    console.log(tmp);
}
