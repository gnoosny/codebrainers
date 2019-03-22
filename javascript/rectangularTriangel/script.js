a = 7;
b = 24;
c = 25;

rectangular = false;

if (Math.pow(a, 2) + Math.pow(b,2) == Math.pow(c,2)) {
	rectangular = true;
}


if (rectangular) {
	console.log("Triangle is rectangular")
} else {
	console.log("Triangle is not rectangular")
}
