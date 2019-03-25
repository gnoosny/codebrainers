let person = {
    name: "Przemek",
    surname: "Leksa",
    showName: function(){
        console.log(this.name + " " + this.surname);
    }
};

person.showName();