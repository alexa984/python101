--task1--
select ADDRESS
from STUDIO
where NAME = 'MGM';

--task2--
select BIRTHDATE
from MOVIESTAR
where NAME = 'Kim Basinger';

--task3--
select NAME
from MOVIEEXEC
where NETWORTH >= 10000000;

--task4--
select NAME
from MOVIESTAR
WHERE GENDER = 'M' or ADDRESS='Prefect Rd';

--task5--
INSERT INTO MOVIESTAR
VALUES ('Zahari Baharov', 'some address', 'M', '1980-12-08' );

--task6--
DELETE FROM STUDIO
WHERE ADDRESS LIKE '%5%';

--task7--
update MOVIE
set STUDIONAME = 'Fox'
where TITLE like '%star%'



