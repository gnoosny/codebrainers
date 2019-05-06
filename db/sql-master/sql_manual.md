# Zapytania SQL

## INSERT

Wstawia nowe wiersze do wybranej tabeli

```SQL
INSERT INTO some_fancy_table (column_with_id, some_column, other_column)
VALUES (1, 'foo', 'bar')
```

## SELECT

Wyświetla zawartość wybranej tabeli

```SQL
SELECT *
FROM some_fancy_table
```

Możesz zawęzić zbiór kolumn zwracanych w wyniku zapytania

```SQL
SELECT some_column, other_column
FROM some_fancy_table
```

Zapytanie SELECT jest znacznie bardziej rozbudowane, więcej szczegółów możesz znaleźć w osobnym rozdziale.

## UPDATE

Modyfikuje *wszystkie* rekordy spełniające podany warunek

```SQL
UPDATE some_fancy_table
SET some_column = 'abc'
WHERE column_with_id > 42
```

## DELETE

Działa podobnie do zapytania `UPDATE` - usuwa *wszystkie* rekordy spełniające podany warunek

```SQL
DELETE FROM some_fancy_table
WHERE column_with_id = 5
```
