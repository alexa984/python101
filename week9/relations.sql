--task1--
select NAME
from MOVIESTAR
where GENDER = 'M' and NAME in (select STARNAME
				from STARSIN
				where MOVIETITLE='Terms of Endearment');
				
--task2--
select STARNAME
from STARSIN
where MOVIEYEAR = 1995 and MOVIETITLE in(
select TITLE
from MOVIE
where STUDIONAME = 'MGM'
);

--task3--
alter table STUDIO
add column PRESIDENT varchar(255) DEFAULT 'The Pope';

select PRESIDENT
from STUDIO
where NAME='MGM'

--task4--
select NAME
from MOVIE
where length >(select length from MOVIE where NAME='Gone With the Wind');

--task5--
select NAME
from MOVIEEXEC
where NETWORTH>(select NETWORTH from MOVIEEXEC where NAME='Merv Griffin');
