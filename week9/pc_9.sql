--task9--
SELECT maker
FROM   product
       JOIN pc
         ON pc.model = product.model
WHERE  pc.price = (SELECT Max(price)
                   FROM   pc)  
