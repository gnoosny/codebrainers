function correctName(name) {
    let newName = "";
    console.log(name)
    newName = name[0].toUpperCase() + name.slice(1);
    return newName;
}

console.log(correctName('adam'))