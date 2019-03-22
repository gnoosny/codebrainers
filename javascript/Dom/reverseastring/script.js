const string = "After 2 years of debates, you will soon be asked to vote on the Proposal for a Directive on copyright in the Digital Single Market. Despite the intense debates, the final text does not include the suggestions for improvements from the analyses that over 70 Internet experts, the UN Special Rapporteur on Freedom of Expression, NGOs, programmers, and academics have stated repeatedly."

console.log('Original string:\n' + string);

let stringNew = string.split("");

console.log(stringNew);

let stringReverse = []

for (let i = stringNew.length; i >= 0 ; i--) {
    stringReverse.push(stringNew[i])
}

stringReverse = stringReverse.join("");
console.log(stringReverse)