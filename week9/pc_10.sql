--task10--
SELECT Avg(hd) AS AVG_HD
FROM   product
       INNER JOIN pc
               ON product.model = pc.model
WHERE  product.maker IN (SELECT maker
                         FROM   product
                         WHERE  type = 'printer')
