--task3--
ALTER TABLE studio
  ADD COLUMN president VARCHAR(255) DEFAULT 'The Pope';

SELECT president
FROM   studio
WHERE  name = 'MGM' 
