--task6--
SELECT Avg(price)
FROM   pc
       JOIN product
         ON pc.model = product.model
WHERE  product.maker = 'A'  
