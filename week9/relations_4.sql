--task4--
SELECT NAME
FROM   movie
WHERE  length > (SELECT length
                 FROM   movie
                 WHERE  NAME = 'Gone With the Wind')  
