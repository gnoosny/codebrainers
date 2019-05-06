Skorzystaj z bazy `simple_library_db.csv`

---

1. Podaj listę wszystkich książek w bibliotece
SELECT DISTINCT field2 FROM simple_library_db

2. Podaj listę książek napisanych przez Stanisława Lema
SELECT DISTINCT field2 FROM simple_library_db
WHERE field3 LIKE '%Lem%'

3. Podaj listę książek zarejestrowanych w 2015 r.
SELECT field2 FROM simple_library_db
WHERE field5 LIKE '2015%'

4. Oblicz liczbę książek w bibliotece
SELECT COUNT(field1) FROM simple_library_db

5. Oblicz, ilu różnych autorów stworzyło książki przechowywane w bibliotece
SELECT COUNT(DISTINCT field3) FROM simple_library_db

6. Dla każdego autora oblicz liczbę egzemplarzy książek przechowywanych w bibliotece
SELECT field3, COUNT(field2) as 'number of books' FROM simple_library_db
GROUP BY field3

7. Oblicz liczbę książek starszych niż 10 lat
SELECT field1, COUNT(field1) as 'number of books older than 10 years old' FROM simple_library_db
WHERE field5 < 2009-04-17


8. Dla każdego autora podaj liczbę tytułów przez niego napisanych
SELECT field3, COUNT(DISTINCT field2) as 'number of titles' FROM simple_library_db
GROUP BY field3