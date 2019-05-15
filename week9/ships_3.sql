--task3--
SELECT ship
FROM   outcomes
       JOIN battles
         ON outcomes.battle = battles.NAME
WHERE  battles.date LIKE '1942%'  
