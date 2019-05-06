select authors.surname, titles.title FROM titles
JOIN authors ON authors.id = titles.author_id