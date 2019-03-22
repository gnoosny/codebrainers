let min = 0;
let max = 1000;
let number = [];
for (let i = 0; i < 10; i++) {
    number.push(Math.floor(Math.random() * (+max - +min)) +min)
}


console.log(number);
let FizzBuzz = 'FizzBuzz'

for (let i = 0; i < number.length; i++) {
    if (number[i] % 3 == 0 && number[i] % 5 == 0) {
        console.log('number ' + number[i] + ' is ' + FizzBuzz)
    } else if (number[i] % 3 == 0) {
        console.log('number ' + number[i] + ' is ' + FizzBuzz.substring(0,4))
    } else if (number[i] % 5 == 0) {
        console.log('numbet ' + number[i] + ' is ' + FizzBuzz.substring(4,FizzBuzz.length))
    } else {
        console.log('number ' + number[i] + ' can\'t be devided by 3 or 5 or both')
    }
}