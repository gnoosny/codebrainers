let end = 22;
let half = end/2;
for (let i = 1; i < end; i++) {
    if (i % 2 != 0 && i % 3 != 0 && i % 5 != 0){
        console.log(i);
    }
}