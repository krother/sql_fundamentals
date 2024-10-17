
# SQL Functions

In the SQL language, there are many functions that do useful things.
You may already have seen **aggregation functions** like `sum()`, `count()` or `avg()`.
In this chapter you will see a few more generic functions.

## Exercise 1: Preparations

Log in to [workspace.hackschule.de](https://workspace.hackschule.de) .

Open a terminal through the menu and type in the terminal window:

    mycli

Make sure that you have the `babynames` table.

## Exercise 2: Execute a function

Execute the query:

    SELECT name, length(name) FROM babynames LIMIT 5;

Also try:

    SELECT name, substr(name, 1, 1) FROM babynames LIMIT 5;

## Exercise 3: Functions in WHERE

Functions can also be used in the `WHERE` clause.

Write a query that shows 10 names with 10 or more characters.

## Exercise 4: Functions in GROUP BY

Find out how many names in 2020 start with which first letter and display the most frequent ones.
Arrange the lines in the following query correctly:

    DESC
    FROM babynames
    GROUP BY first
    LIMIT 10
    ORDER BY count(name)
    SELECT substr(name, 1, 1) AS first, count(name)
    WHERE year = 2020
    ;

## Exercise 5: Last Letters

Look up the documentation of the `substr()` function on [www.w3schools.com/mysql](https://www.w3schools.com/mysql/mysql_ref_functions.asp). Find out how to extract the last letter from the name.

## Exercise 6: Letter Combinations

Modify the query from Exercise 4 so that you find out the most frequent first/last letter combination.
You need to modify the `GROUP BY` part:

    GROUP BY first, last

and the select part:

    SELECT substr(name, 1, 1) AS first, substr(...) AS last, count(name)

## Exercise 7: Documentation

Go to the documentation on [www.w3schools.com/mysql](https://www.w3schools.com/mysql/mysql_ref_functions.asp) and find functions that:

- converts a string to lower case
- reverses a string

Write a short example query.

#### Hint: Functions in Spark SQL

Some functions in Spark/Databricks SQL differ slightly.
You find a complete list on [https://spark.apache.org/docs/latest/api/sql/](https://spark.apache.org/docs/latest/api/sql/)

## Exercise 8: Palindromes

Find names that are **palindromes** (they are the same if read back-to-front).
Complete the query:

    SELECT DISTINCT name
    FROM babynames
    WHERE ... = ...
    LIMIT 10;
    