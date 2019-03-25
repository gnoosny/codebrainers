function sum (a, b) {
    return a + b;
}

let zmiennaA = 5;
let zmiennaB = 9;

let suma = sum(zmiennaA, zmiennaB);

console.log(suma);

function newSum() {
    let sum = 0;
    for (let i = 0; i < arguments.length; i++) {
        sum += arguments[i];
    }
    return sum
}

console.log(newSum(1, 2, 3, 4, 5));
