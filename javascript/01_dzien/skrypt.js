console.log('Hello world');

const pi = 3.14;
let surname = 'Leksa'

console.log(pi);

console.log(surname)

surname = 'Kowalski'

console.log(surname)

let days = 31;
let daysString = '31'

if(days === daysString) {
    console.log('wartosci sa rowne')
} else {
    console.log('wartosci sa rozne')
}

let zmienna1 = 3
let zmienna2 = 5
let liczba = 17

if (liczba%zmienna1 === 0 && liczba%zmienna2 === 0) {
    console.log('liczba jest podzielna przez trzy i piec')
} else if (liczba%zmienna2 === 0){
    console.log('liczba jest podzielna przez 3')
} else if (liczba%zmienna2 === 0) {
    console.log('liczba jest podzielna przez 5')
} else {
    console.log('liczba nie jest podzielna ani przez 3 ani przez 5')
}

//polecenie typeof

if (typeof zmienna1 ==  "number") {
    console.log('zmienna1 jest liczba')
}

if (typeof zmienna6 =="undefined") {
    console.log('zmienna6 nie istnieje')
}

let name = 'Przemek';
surname = 'Leksa';
let fullName = name + ' ' + surname;

console.log(fullName);

let year = 2019;
year = "rok 2019";

console.log(parseInt("21px") + 21);

console.log(name.length);

let tablica = [1, 2, 3];
console.log(tablica[0]);

console.log(tablica[tablica.length - 1]);

tablica.push(4);
tablica.unshift(0);
console.log(tablica);

tablica.shift();
tablica.pop();
console.log(tablica);

for (let i = 0; i < tablica.length; i++) {
    console.log(tablica[i]);
}
let gwiazdka =""
for (let i = 0; i < 20; i++){
    gwiazdka +="*"
    console.log(gwiazdka)
}

let znak = ""

for (let i = 0; i < 20; i++) {
    if (i%2 != 0) {
        znak += "*"
    } else {
        znak += "|"
    }
    console.log(znak)
}

let text = "";
for (let i = 0; i < 10; i++) {
    for (let j = 0; j < 10; j++){
        text += "*"
    }
    text += "\n"
}

console.log(text)

let szachownica = ""
for (let i = 0; i < 8; i++){
    for (let j = 0; j < 8; j++){
        if (j % 2 == 0 && i % 2 != 0) {
            szachownica += "B"
        } else if (j % 2 != 0 && i % 2 != 0 ) {
            szachownica += "C"
        }
        if (j % 2 == 0 && i % 2 == 0) {
            szachownica += "C"
        } else if (j % 2 != 0 && i % 2 == 0 ) {
            szachownica += "B"
        }
    }
    szachownica += "\n"
}

console.log(szachownica)

let kwadrat = ""
for (let i = 0; i < 20; i++){
    if (i == 0 || i == 19) {
        kwadrat += "***************\n"
    } else {
        kwadrat += "*             *\n"
    }
}

console.log(kwadrat)

let kw =""

for (let i = 0; i < 20; i++) {
    if (i == 0 || i == 19) {
        kw += "********************\n"
    }
    for (let j = 0; j < 20; j++) {
        if (j == 0 && i!= 19) {
            kw += "*"
        } else if (j == 19 && i!= 19) {
            kw += "*\n"
        } else {
            kw += " "
        }
    }
}
console.log("przerwa")
console.log(kw)

let cross = ""
let start = 0
let end = 10
for (let i = 0; i < 11; i++){
    let cross = ""
    for (let j = 0; j < 11; j++){
        if (i == j && j != end) {
            cross += "*"
        } 
        if (j == end) {
            cross +="*"
            end -=1
        }
        
        else {
            cross += " "
        }
    }
   
   console.log(cross)
}

console.log(cross)