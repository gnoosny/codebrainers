let string = "Eva, can I see bees in a cave?"
let regex = /\w/g;
let result = string.toLowerCase().match(regex);



let reversed = [];

for (let i = 0; i < result.length; i++) {
    reversed.unshift(result[i])
}
console.log(result);
console.log(reversed);

if (result == reversed) {
    console.log('The string is a palindrome')
} else {
    console.log('The string is not a palindrome')
}

result = result.join("");
reversed = reversed.join("");

console.log(result);
console.log(reversed);

if (result == reversed) {
    console.log('The string is a palindrome')
} else {
    console.log('The string is not a palindrome')
}