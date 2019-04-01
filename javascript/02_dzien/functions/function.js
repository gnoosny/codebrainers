function showText() {
    console.log("to jest cialo funkcji")
}

showText();

function isNumber(number, convert) {
    let tmp = number;
    console.log(convert)
    if (convert === true) {
        tmp = parseInt(tmp);
    }
    
    if (typeof tmp === "number" && !isNaN(tmp)) {
        console.log("to jest numer " + tmp)
    } else {
        console.log("to nie jest numer")
    }
}

isNumber(4);
isNumber("zupa", true);
isNumber("123", true);
isNumber("123");

