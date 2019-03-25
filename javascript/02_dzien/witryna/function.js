function showText() {
    console.log("To jest ciało naszej fukcji");
}

//showText();

function isNumber(number, convert = false) {
    console.log(convert);

    let tmp = number;

    if (convert === true) {
        tmp = parseInt(tmp);
    }

    if (typeof tmp === "number" && !isNaN(tmp)) {
        console.log("To jest numer")
    } else {
        console.log("To nie jest numer");
    }
}

//isNumber("sdsad", true);

function sum(a, b) {
    return a + b;
}

let zmiennaA = 5;
let zmiennaB = 9;

let suma = sum(zmiennaA, zmiennaB);
//console.log(suma);

function newSum() {
    let sum = 0;
    for (let i = 0; i < arguments.length; i++) {
        sum += arguments[i];
    }
    return sum;
}

//console.log(newSum(1, 2, 3, 4, 5));


function silnia(liczba) {
    //console.log(liczba)
    let silnia = 1;
    if (liczba < 0) {
        return "Liczba spoza zakresu"

    }
    else if (liczba === 0) {
        return silnia;

    }
    else {
        for (let i = liczba; i != 0; i--) {
            //console.log(i);
            silnia = silnia * i;
        }

        return silnia;

    }

}
//silnia(5);
//console.log(silnia(3));













function sredniaWazona(sprawdziany, kartkowki, aktywnosc, prezentacje) {
    let licznik = 0;
    const wagi = [0.5, 0.25, 0.2, 0.05]
    let mianownik = (sprawdziany.length * wagi[0]) + (kartkowki.length * wagi[1]) + (aktywnosc.length * wagi[2]) + (prezentacje.length * wagi[3]);
    //return mianownik
    for (let i = 0; i < sprawdziany.length; i++) {
        licznik += sprawdziany[i] * wagi[0];
    }
    for (let i = 0; i < kartkowki.length; i++) {
        licznik += kartkowki[i] * wagi[1];
    }
    for (let i = 0; i < aktywnosc.length; i++) {
        licznik += aktywnosc[i] * wagi[2];
    }
    for (let i = 0; i < prezentacje.length; i++) {
        licznik += prezentacje[i] * wagi[3];
    }
    return licznik / mianownik
}


//console.log(sredniaWazona([6, 6], [6, 6], [6], [6]))


function correctName(name) {
    let newName = "";
    newName = name[0].toUpperCase();
    newName += name.slice(1);
    return newName;
}

//console.log(correctName('adam'));

let person = {
    name: "Piotr",
    surname: "Arciszewski",
    showName: function () {
        console.log(this.name + " " + this.surname);
    }
};

person.showName();
