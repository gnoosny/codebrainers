Skorzystaj z bazy `library_db.sql`

---

Dodatkowe informacje:
  
  * maksymalny czas wypożyczenia - 25 dni
  * opłata za każdy dzień zwłoki - 0,50 PLN

---

1. Oblicz liczbę użytkowników biblioteki
SELECT COUNT(id) FROM users

2. Oblicz liczbę użytkowników biblioteki aktywnych w 2018 r.
SELECT COUNT (DISTINCT users.id) FROM users
JOIN borrowings ON users.id = borrowings.user_id
WHERE borrowings.borrow_date LIKE '2018%'

3. Podaj listę użytkowników, którzy w 2010 r. pożyczyli więcej niż 3 książki
SELECT borrowings.user_id, users.surname, users.name FROM borrowings
JOIN users ON users.id = borrowings.user_id
WHERE borrowings.borrow_date LIKE '2010%'
GROUP BY users.id
HAVING COUNT(borrowings.book_id) > 3

4. Oblicz liczbę książek pożyczonych przez każdego z użytkowników.
SELECT borrowings.user_id, users.name, users.surname, COUNT(borrowings.book_id) as 'wypozyczenia' FROM borrowings
JOIN users ON users.id = borrowings.user_id
GROUP BY users.ID

5. Oblicz liczbę książek pożyczonych przez każdego z użytkowników w 2017 r.
SELECT borrowings.user_id, users.name, users.surname, COUNT(borrowings.book_id) as 'wypozyczenia' FROM borrowings
JOIN users ON users.id = borrowings.user_id
WHERE borrowings.borrow_date LIKE '2017%'
GROUP BY users.ID

---

6. Podaj łączną liczbę wypożyczeń każdego egzemplarza
SELECT borrowings.user_id, users.name, users.surname, COUNT(borrowings.book_id) as 'wypozyczenia' FROM borrowings
JOIN users ON users.id = borrowings.user_id
WHERE borrowings.borrow_date LIKE '2017%'
GROUP BY users.ID

7. Podaj łączną liczbę wypożyczeń każdego tytułu
SELECT borrowings.book_id, COUNT(*) FROM borrowings
GROUP BY borrowings.book_id

8. Podaj 10 najpopularniejszych tytułów w 2016 r.
SELECT titles.title, COUNT(*) FROM borrowings
JOIN books ON borrowings.book_id = books.ID
JOIN titles ON books.title_id = titles.id
WHERE STRFTIME('%Y', borrowings.borrow_date)= '2016'
group by titles.title
order by COUNT(*) DESC
LIMIT 10

---

9. Podaj listę pozycji (tytuł, ID egzemplarza, imię i nazwisko użytkownika) oddanych po terminie
SELECT titles.title, books.id, users.name, users.surname FROM users
JOIN borrowings ON users.id = borrowings.user_id
JOIN books ON books.id = borrowings.book_id
JOIN titles ON books.title_id = titles.id
WHERE julianday(borrowings.return_date) - julianday(borrowings.borrow_date) > 25

10. Podaj listę pozycji (tytuł, ID egzemplarza, imię i nazwisko użytkownika, liczba dni) oddanych po terminie
SELECT titles.title, books.id, users.name, users.surname, julianday(borrowings.return_date) - julianday(borrowings.borrow_date) as 'liczba dni' FROM users
JOIN borrowings ON users.id = borrowings.user_id
JOIN books ON books.id = borrowings.book_id
JOIN titles ON books.title_id = titles.id
WHERE julianday(borrowings.return_date) - julianday(borrowings.borrow_date) > 25


11. Podaj listę pozycji (tytuł, ID egzemplarza, imię i nazwisko użytkownika) nieoddanych
SELECT titles.title, books.id, users.name, users.surname from users
JOIN borrowings ON users.id = borrowings.user_id
JOIN books ON books.id = borrowings.book_id
JOIN titles ON books.title_id = titles.id
WHERE borrowings.return_date IS NULL

---

12. Podaj 20 najdłużyszych zakończonych wypożyczeń
SELECT titles.title, books.id, users.name, users.surname, julianday(borrowings.return_date) - julianday(borrowings.borrow_date) as liczba_dni FROM users
JOIN borrowings ON users.id = borrowings.user_id
JOIN books ON books.id = borrowings.book_id
JOIN titles ON books.title_id = titles.id
WHERE liczba_dni > 25
ORDER BY liczba_dni DESC
LIMIT 20

13. Podaj 10 najdłuższych niezakończonych wypożyczeń
SELECT titles.title, books.id, users.name, users.surname, julianday('now') - julianday(borrowings.borrow_date) as liczba_dni FROM users
JOIN borrowings ON users.id = borrowings.user_id
JOIN books ON books.id = borrowings.book_id
JOIN titles ON books.title_id = titles.id
WHERE borrowings.return_date IS NULL
ORDER BY liczba_dni DESC
LIMIT 10


---

14. Oblicz średnią liczbę dni wypożyczenia dla każdego użytkownika
SELECT users.name, users.surname, avg(julianday(borrowings.return_date) - julianday(borrow_date)) as sredni_czas_wypozyczenia FROM users
JOIN borrowings ON users.id = borrowings.user_id
GROUP BY users.name

15. Oblicz łączną liczbę dni wypożyczenia ponad termin dla każdego użytkownika
SELECT users.name, users.surname, sum(IFNULL(julianday(borrowings.return_date), julianday('now')) - julianday(borrowings.borrow_date) - 25) as liczba_dni FROM users
JOIN borrowings ON borrowings.user_id = users.id
Where IFNULL(julianday(borrowings.return_date), julianday('now')) - julianday(borrowings.borrow_date) > 25
Group by users.id

16. Oblicz średnią liczbę dni wypożyczenia ponad termin dla każdego użytkownika
SELECT users.name, users.surname, avg(IFNULL(julianday(borrowings.return_date), julianday('now')) - julianday(borrowings.borrow_date) - 25) as srednia_liczba_dni FROM users
JOIN borrowings ON borrowings.user_id = users.id
Where IFNULL(julianday(borrowings.return_date), julianday('now')) - julianday(borrowings.borrow_date) > 25
Group by users.id

---

17. Podaj 10 tytułów, które średnio są wypożyczane na największą liczbę dni
SELECT books.id, titles.title, avg(IFNULL(julianday(borrowings.return_date), julianday('now')) - julianday(borrowings.borrow_date)) as srednia_liczba_dni FROM books
JOIN titles ON titles.id = books.title_id
JOIN borrowings ON books.id = borrowings.book_id
GROUP BY titles.title
ORDER BY srednia_liczba_dni DESC
LIMIT 10

18. Podaj 10 tytułów, które były najdłużej wypożyczone


19. Podaj 10 tytułów, które były najdłużej wypożyczone (uwzględnij wypożyczenia, które nadaj trwają)
SELECT books.id, titles.title, sum(IFNULL(julianday(borrowings.return_date), julianday('now')) - julianday(borrowings.borrow_date)) as suma from books
JOIN titles ON books.title_id = titles.id
JOIN borrowings ON books.id = borrowings.book_id
GROUP BY titles.title
ORDER BY suma DESC
LIMIT 10

---

20. Oblicz łączną kwotę zapłaconą przez każdego z użytkowników
SELECT users.name, users.surname,  sum(fines.fine) as suma_grzywny FROM users
JOIN fines ON users.id = fines.user_id
group by users.name

21. Oblicz łączną kwotę, który każdy użytkownik powinien był zapłacić


22. Podaj listę użytkowników zalegających z opłatami
23. Oblicz dług każdego użytkownika zalegającego z opłatami

---

24. Podaj średnią liczbę wypożyczeń egzemplarzy każdego z tytułów
25. Podaj średnią liczbę wypożyczeń tytułów każdego z autorów
26. Podaj średnią liczbę wypożyczeń egzemplarzy każdego z autorów

---

27. Podaj najpopularniejszego autora dla każdego użytkownika
28. Podaj najaktywniejszego użytkownika dla każdego autora
