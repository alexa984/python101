--task1--
select NAME
from MOVIESTAR
where GENDER = 'M' and NAME in (select STARNAME
				from STARSIN
				where MOVIETITLE='Terms of Endearment');