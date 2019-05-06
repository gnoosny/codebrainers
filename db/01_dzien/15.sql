SELECT author, count(author) as count FROM books
WHERE author IS NOT NULL
GROUP BY author
HAVING count(author) > 1