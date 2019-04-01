function silnia(liczba) {
    if (liczba < 0) {
        return "liczba jest mniejsza od zera";
    } else if (liczba === 0) {
        return 1;
    } else {
        let silnia = 1;
        for (let i = liczba; i > 0; i--){
            silnia *= i;
            console.log(liczba)
        }
        return silnia;
    }
}

console.log(silnia(-1))
console.log(silnia(0))
console.log(silnia(5))