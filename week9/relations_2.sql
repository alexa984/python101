--task2--
SELECT starname
FROM   starsin
WHERE  movieyear = 1995
       AND movietitle IN(SELECT title
                         FROM   movie
                         WHERE  studioname = 'MGM')  
