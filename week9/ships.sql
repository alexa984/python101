--task1--
select NAME, country, numguns, LAUNCHED
from ships join classes on ships.class = CLASSES.class;

--task2--
select NAME, country, numguns, LAUNCHED
from CLASSES left join ships on ships.class = CLASSES.class;

--task3--
select SHIP
from OUTCOMES join battles on outcomes.BATTLE=BATTLES.NAME
where BATTLES.DATE LIKE '1942%' ;

--task4--
select CLASSES.COUNTRY, SHIPS.NAME
from SHIPS join CLASSES on ships.CLASS=CLASSES.CLASS
where ships.NAME not in (select ship from OUTCOMES)
order by CLASSES.COUNTRY