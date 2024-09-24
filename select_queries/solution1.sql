-- what benefits does a database offer?
-- Overview of relational databases: PostGreS, MySQL and others
-- accessing a database on a remote machine

-- key parts of SELECT queries: FROM, WHERE, ORDER BY, LIMIT, OFFSET
-- aggregation with GROUP BY and HAVING
-- aggregation functions
-- arithmetic and statistical functions
-- binning data
-- sampling
-- vertical joins with UNION

CREATE DATABASE day1;
USE day1;

CREATE TABLE babynames (
    year INT,
    name VARCHAR(100),
    gender VARCHAR(1),
    births INT
);

SHOW TABLES;
DESCRIBE babynames;

SELECT * FROM babynames;

SELECT name, births FROM babynames;

SELECT year, births FROM babynames WHERE name='George';

SELECT name, births FROM babynames WHERE births = 100;

SELECT name, births FROM babynames WHERE births >= 10000;

SELECT name, births FROM babynames WHERE births BETWEEN 10000 AND 11000;

SELECT name, births FROM babynames WHERE year=2009 AND gender='F' ORDER BY births DESC LIMIT 5;

SELECT name, births FROM babynames WHERE year=2009 AND gender='F' ORDER BY births DESC LIMIT 5 OFFSET 4;

-- aggregation
SELECT sum(births) FROM babynames;
-- count, min, max, avg, std

-- arithmetics
SELECT name, births * 100 FROM babynames LIMIT 5;

SELECT name, round(births / 100, 2) FROM babynames LIMIT 5;

SELECT * FROM babynames WHERE births % 777 = 0;

SELECT name, pow(births, 2) FROM babynames WHERE births = 5 LIMIT 5;
SELECT name, log(births) FROM babynames WHERE births = 5 LIMIT 5;
SELECT name, exp(births) FROM babynames WHERE births = 5 LIMIT 5;

-- rename
SELECT sum(births) total FROM babynames;

-- union
-- same columns in same order
-- parentheses matter
(SELECT name, births FROM babynames WHERE year=2009 AND gender='F' AND births > 10000 ORDER BY births DESC LIMIT 5)
UNION
(SELECT name, births FROM babynames WHERE year=2009 AND gender='M' AND births > 10000 ORDER BY births DESC LIMIT 5)
;

--
-- more complex patterns
--

-- percentage
SELECT name, births,
       births * 100.0 / (SELECT sum(births) FROM babynames) AS percentage
FROM babynames
WHERE year=2009 LIMIT 5;

-- sample
--   slow!!!
SELECT * FROM babynames ORDER BY RAND() LIMIT 10;

-- faster variant in Spark SQL:
-- SELECT * FROM babynames TABLESAMPLE (10 ROWS);

-- also faster: select 0.1% of the data
SELECT * FROM babynames WHERE RAND() <= 0.001;

-- quartiles
WITH quartiles AS (
    SELECT 
        births,
        NTILE(4) OVER (ORDER BY births) AS quartile
    FROM babynames
)
SELECT 
    quartile,
    MIN(births) AS min_value,
    MAX(births) AS max_value
FROM quartiles
GROUP BY quartile
ORDER BY quartile;

-- task: 10 bins, median
