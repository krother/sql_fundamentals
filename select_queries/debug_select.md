
# Debugging SELECT Queries

## Part 1: Syntax Errors

**Syntax errors** are fundamental spelling and grammar mistakes when writing queries.
They result in the database not being able to understand a command at all.
As a result, nothing gets done.
Typical reasons for syntax errors are misspelled keywords, missing brackets or wrong order of language elements.

Find one bug in each query:

### 1.1

SLECT * FROM babynames LIMIT 5; 

### 1.2

SELECT name LIMIT 10;

### 1.3

SELECT * FROM babynames OFFSET 4 LIMIT 5 ;

### 1.4

SELECT * FROM babynames WHERE name="George";

### 1.5

SELECT name births year FROM babynames LIMIT 5;

### 1.6

SELECT name AS baby births AS count FROM babynames;

### 1.7

SELECT * FROM babynames 
WHERE name='Emily' AND births GREATER THAN 10000;

### 1.8

SELECT * FROM babynames 
WHERE name='Diana' AND births BETWEEN 100-2000;

### 1.9

SELECT sum(births FROM babynames LIMIT 5;

### 1.10

SELECT name, births 
FROM babynames 
ORDER BY births
WHERE year = 2023 AND gender = 'M' 
LIMIT 10;


## Part 2: Semantic Errors

In a **Semantic error**, the command is formally correct.
However, it does not deliver the result you expected.
Semantic errors are due to the logic of the query.

Find and fix the bugs in each query:

### 2.1

-- find all boys named Robin from 100+ years ago
SELECT * FROM babynames WHERE name='Robin' ORDER BY year DESC;

### 2.2

-- find out the ten most frequent names in 2020
SELECT name FROM babynames 
WHERE year=2020
ORDER BY births
LIMIT 10;

### 2.3

-- find out the number of babies for the ten most frequent names in 2020
SELECT name births FROM babynames
WHERE year=2020
ORDER BY births
LIMIT 10;

### 2.4

-- calculate the total number of babies for 2023
SELECT sum(name) FROM babynames;

### 2.5

-- find names that occur 4000-4005 times
SELECT * FROM babynames WHERE births < 4000 AND births > 4005;


## Part 3 Aggregation Errors

The `GROUP BY` statement is a bit trickier than the other parts of queries.
Here are a few buggy statements specific for that one.

Fix the syntactic and semantic errors:

### 3.1

    -- total number of boys for each year
    SELECT year, sum(births) FROM babynames GROUP BY year WHERE gender='M';

### 3.2

-- total number of girls/boys
SELECT gender, year, sum(births) FROM babynames GROUP BY gender;

### 3.3

-- number of births for the top name for each year
SELECT year, max(births) FROM babynames GROUP BY max(births) ORDER BY year DESC;

### 3.4

-- number of different names for each year/gender combination for each year ending with a zero.
SELECT year, gender, count(name) FROM babynames WHERE year % 10 = 0;

### 3.5

-- names with more than 4M births over all the US history
SELECT name, sum(births) FROM babynames WHERE sum(births) > 4000000 GROUP BY name ORDER BY sum(births) DESC;
