# Zapytanie SELECT

## SELECT FROM

Wyświetla zdefiniowane kolumny z danej tabeli

```SQL
SELECT name, surname FROM authors
```

## WHERE

Odrzuca rekordy, które nie spełniają warunku

```SQL
SELECT * FROM fines
    WHERE fine > 3,5
```

```SQL
SELECT * FROM authors
    WHERE surname LIKE "Lem"
```

Watunki można łączyć wyrażeniami ```AND``` i ```OR```

## GROUP BY

Oblicza agregaty - funkcje obliczane dla zbiorów wierszy. Np. gdy chcemy policzyć książki napisane przez każdego autora autora:

```SQL
SELECT author_id, count(title) FROM titles
    GROUP BY author_id
```

Istnieje kilka agregatów:

 * `count()` - zlicza elementy
 * `sum()` - dodaje elementy
 * `min()`, `max()`, `avg()` - obliczają odpowiednio wartość najmniejszą, największą i średnią

 Dokumenraacja: http://www.sqlitetutorial.net/sqlite-aggregate-functions/

## HAVING

Filtruje rekordy na podstawie wartości agregatów - analogicznie jak `WHERE` filtruje na podstawie wartości pojedynczych pól

```SQL
SELECT author_id, count(title) FROM titles
    GROUP BY author_id
    HAVING count(title) > 15
```

## ORDER BY

Umożliwia sortowanie wyniku zapytania po dowolnej kolumnie. Jeśli przekażemy mu kilka kolumn, wynik zostanie posortowany najpierw po pierwszej, a gdy wartości pierwszej kolumny są równe - po kolejnej. `ORDER BY` umożliwia także sortowanie po wartości agregatów

```SQL
SELECT * FROM authors
    ORDER BY surname, name
```

### DESC

Sortuje wynik w kolejności malejącej

```SQL
SELECT * FROM authors
    ORDER BY surname DESC
```

## LIMIT

Zwraca kilka pierwszych wyników zapytania

```SQL
SELECT * FROM users
    ORDER BY surname
    LIMIT 20
```

## DISTINCT

Zwraca w wyniku rekordy bez powtórzeń

```SQL
SELECT DISTINCT surname FROM users
```

Może być także użyte w agregatach

```SQL
SELECT surname, count(DISTINCT name) FROM users
```

## JOIN

Łączy rekordy z dwóch kolumn w jeden na podstawie podanego warunku

```SQL
SELECT * FROM authors
    JOIN titles ON authors.ID == titles.author_id
```

## Obsługa dat

Daty w SQLite są przechowywane jako napisy. Przed "użyciem" należy je przekształcić do odpowiedniego formatu. Najlepiej opisuje to dokumentacja: https://www.sqlite.org/lang_datefunc.html