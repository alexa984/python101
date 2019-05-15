--task2--
SELECT maker,
       Avg(screen)
FROM   laptop
       JOIN product AS p
         ON laptop.model = p.model
GROUP  BY maker
