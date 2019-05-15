--task8--
SELECT maker
FROM   product
WHERE  type = 'PC'
GROUP  BY maker
HAVING Count(model) >= 3  
