--task1--
select AVG(speed)
from pc;

--task2--
select maker, AVG(screen)
from laptop
join product as p on laptop.model = p.model
group by maker;

--task3--
select AVG(speed)
from laptop
where price>1000;

--task4--
select hd, AVG(price)
from pc
group by hd;

--task5--
select AVG(speed)
from pc
where speed > 500;

--task6--
select AVG(price)
from pc join product on pc.model=product.model
where product.maker = 'A';

--task7--
select AVG(price)
from (
select price
from pc join product on pc.model=product.model
where product.maker = 'B'

union all

select price
from laptop
join product on laptop.model=product.model
where product.maker = 'B');

--task8--
select maker
from product
where type = 'PC'
group by maker
having COUNT(model) > 3;

--task9--
select maker
from product join pc on pc.model = product.model
where pc.price = (select max(price) from pc);

--task10--
SELECT AVG(hd) AS AVG_HD
FROM pc 
JOIN product p ON pc.model = p.model
WHERE maker in (
SELECT DISTINCT maker
FROM product p JOIN printer pr ON p.model = pr.model)
