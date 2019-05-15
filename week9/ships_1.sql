--task1--
SELECT NAME,
       country,
       numguns,
       launched
FROM   ships
       JOIN classes
         ON ships.class = classes.class;  
