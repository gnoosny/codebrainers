/*
 To jest komentarz wielolinijkowy
*/

//komentarz jednolinijkowy
/*
const pi = 3.14;
pi = 3.15;

let surname = 'Arciszewski';

console.log(surname);

surname = 'Matysiak';

console.log(surname);


let days = 31;
let daysString = "31";

if (days === daysString) {
    console.log("Wartości są równe");
} else {
    console.log("Wartości są różne");
}

let zmienna1 = 3;
let zmienna2 = 5;
let zmienna3 = 15;

if (zmienna3 % zmienna1 === 0) {
    console.log("Liczba podzielna przez 3")
}

if (zmienna3 % zmienna2 === 0) {
    console.log("Liczba podzielna przez 5")
}

//poleceni typeof

if (typeof zmienna1 != "") {
    console.log('Nasza zmienna jest liczba')
}


let name = "Piotr";
let surname = "Arciszewski";

let fullName = name + " " + surname;

console.log(fullName);

let year = 2019;
year = "rok 2019";

console.log("Kot" + "Kot");

console.log("Kot" + true);
console.log("Kot" + 20);

console.log(parseInt("kot") + 21);

console.log(name.length);

let tablica = [1, 2, 3];

tablica.push(4);
tablica.unshift(0);
tablica.shift();
tablica.pop();

console.log(tablica[tablica.length - 1]);
console.log(tablica[0]);

for (let i = 0; i < tablica.length; i++) {
    console.log(tablica[i]);
}


let gwiazdka = "";

for (let i = 0; i < 20; i++) {
    if (i % 2 != 0) {
        gwiazdka += "*"; // gwiazdka = gwiazdka + "*"
    } else {
        gwiazdka += "|"
    }
}
let text = "";
for (let i = 0; i < 10; i++) {
    for (let j = 0; j < 10; j++) {
        text += "*";
    }
    text += "\n";
}

console.log(text);

let wiersz = "";
for (let i = 0; i < 10; i++) {
    for (let j = 0; j < 10; j++) {
        if (i % 2 != 0) {
            if (j % 2 != 0) {
                wiersz += "*"
            }
            else {
                wiersz += "+";
            }
        }
        else {
            if (j % 2 != 0) {
                wiersz += "+"
            }
            else {
                wiersz += "*";
            }
        }
    }
    wiersz += "\n"
}

console.log(wiersz)
*/
let linijka = "";

for (let i = 0; i < 10; i++) {
    for (let j = 0; j < 10; j++) {
        if (i == 0 || i == 9) {
            linijka += "*"
        }
        else {
            if (j != 0 && j != 9) {
                linijka += " "
            }
            else {
                linijka += "*"
            }
        }
    }
    linijka += "\n"
}

console.log(linijka)



let end = 10
for (let i = 0; i < 11; i++) {
    let strTmp = ""
    for (let j = 0; j < 11; j++) {
        if (j == i && j != end) {
            strTmp += "*"
        }
        if (j == end) {
            strTmp += "*"
            end = end - 1
        }
        else {
            strTmp += " "
        }
    }
    console.log(strTmp)
}



