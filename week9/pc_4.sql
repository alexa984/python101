--task4--
SELECT hd,
       Avg(price)
FROM   pc
GROUP  BY hd
