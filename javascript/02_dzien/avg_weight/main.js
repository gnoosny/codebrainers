function averageWeight (sprawdziany, kartkowki, aktywnosc, prezentacje) {
    const weight = [0.5, 0.25, 0.2, 0.05];
    let licznik = 0;
    let mianownik = sprawdziany.length * weight[0] + kartkowki.length *  weight[1] + aktywnosc.length * weight[2] + prezentacje.length * weight[3];
    console.log(mianownik);
    
    for (let i = 0; i < sprawdziany.length; i++) {
        licznik += sprawdziany[i] * weight[0];
    }
    for (let i = 0; i < kartkowki.length; i++) {
        licznik += kartkowki[i] * weight[1];
    }
    for (let i = 0; i < aktywnosc.length; i++) {
        licznik += aktywnosc[i] * weight[2];
    }
    for (let i = 0; i < prezentacje.length; i++) {
        licznik += prezentacje[i] * weight[3];
    }
    return licznik / mianownik;
}

console.log(averageWeight([6],[6],[6],[6]))