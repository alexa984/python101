--task4--
SELECT classes.country,
       ships.NAME
FROM   ships
       JOIN classes
         ON ships.class = classes.class
WHERE  ships.NAME NOT IN (SELECT ship
                          FROM   outcomes)
ORDER  BY classes.country  
