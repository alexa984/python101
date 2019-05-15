--task5--
SELECT NAME
FROM   movieexec
WHERE  networth > (SELECT networth
                   FROM   movieexec
                   WHERE  NAME = 'Merv Griffin')
