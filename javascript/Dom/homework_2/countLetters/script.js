let words = "Podczas gdy inne metody usuwają włosy jedynie tymczasowo, po czym w widoczny sposób zaczynają one odrastać, urządzenie Braun Silk-expert IPL BD5009 oddziałuje na źródło problemu, czyli cebulki włosów – po wstępnym goleniu usypia mieszek włosowy, zatrzymując cykl odrastania włosów. Efektem jest trwałe, widoczne usunięcie owłosienia i nieskazitelny wygląd skóry. Lampa depilatora Braun oferuje żywotność 300 tys. błysków, co przekłada się na długoletnią eksploatację.";

let regex = /\w/g;

let result = words.toLowerCase().match(regex);

console.log(result);

let howMany = {};


for (let i = 0; i < result.length; i++) {
	let letter = result[i]
	if ([result[i]] in howMany){
		howMany[result[i]] += 1;
	} else {
		howMany[result[i]] = 1;
	}
}

console.log(howMany);
