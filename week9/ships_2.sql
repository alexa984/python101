--task2--
SELECT NAME,
       country,
       numguns,
       launched
FROM   classes
       LEFT JOIN ships
              ON ships.class = classes.class
