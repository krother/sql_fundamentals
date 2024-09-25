
# Read Baby Name Data

![Baby Names](baby.png)

## The Dataset

The US authorities have registered the names of all US citizens born
since 1880. The record is `publicly available <http://www.ssa.gov/oact/babynames/limits.html>`__.

In this and the following chapters, you will analyze this data. If
you want to use the ``pandas`` library, you find a list of useful
functions at the bottom.

## Preparations

Log into hackschule.de

You should see

Download the file by typing into the terminal at the bottom of the screen:

    wget URL

    mysql < babynames.sql

Connect to the SQL database with:

    mycli

You should see the prompt

    mysql>

## Inspect the database

Type the following command into the prompt:

    SHOW TABLES;

Press <Enter>. You should see there is one table `babynames`.

You can display the columns of the table with:

    DESCRIBE babynames;

## SELECT queries

In this section, we will go through basic parts of `SELECT`, the most important SQL command.

### Exercise 1: Select everything

SELECT * FROM babynames;

### Exrcise: Limit output

Display the first 5 rows only:

    SELECT * FROM babynames LIMIT 5;

### Exercise 8: Paging

Add the following term to the very end of a query

    LIMIT 5 OFFSET 4

Also inspect the 3rd or 4th "page".

### Exercise 2: Select columns

SELECT name, amount FROM babynames;

### Exercise 3: Select rows

SELECT * FROM babynames WHERE name='George';

Edit the query to select only the `amount` column.

### Exercise 4: Edit the query

Check if your name occurs in the data.
(Names with fewer than 100 occurences have been removed from the data).

### Exercise 5: Filtering with numbers

Other examples of row selection are:

* `WHERE amount = 100`
* `WHERE amount >= 10000`
* `WHERE amount BETWEEN 10000 AND 11000`
* `WHERE amount = 100 AND gender = 'F'`

Find out how many times the name **Taylor** occured in each year since 2000.

### Exercise 6: Sorting

What is the difference between the two queries:

SELECT name, amount FROM babynames WHERE year=2023 ORDER BY name;

and

SELECT name, amount FROM babynames WHERE year=2023 ORDER BY amount DESC;

### Exercises

Find out:

- the 10 most popular girls names in 2023
- the 10 most popular boys names in 2023
- the most frequently occuring name in any single year


### Exercise 10: Celebrities

Investigate the popularity of the names of some US celebrities over the last 130 years.
Inspect the following celebrities or choose your own:

======== ==========================================
name     comment
======== ==========================================
Madonna  wrote “Like a Prayer”
Lance    went to the moon
Katrina  hurricane in New Orleans
Luke     Jedi
Leia     princess from Star Wars
Frida    painter, biography went on a Broadway show
Arielle  mermaid
Khaleesi job title in ‘Game of Thrones’
======== ==========================================

### Exercise 11: Timeline

Inspect the timeline of your own name.



## Arithmetics

SQL has a collection of standard math functions:

SELECT name, amount * 100 FROM babynames LIMIT 5;

SELECT name, round(amount / 100, 2) FROM babynames LIMIT 5;

SELECT * FROM babynames WHERE amount % 777 = 0;

SELECT name, pow(amount, 2) FROM babynames WHERE amount = 5 LIMIT 5;
SELECT name, log(amount) FROM babynames WHERE amount = 5 LIMIT 5;
SELECT name, exp(amount) FROM babynames WHERE amount = 5 LIMIT 5;



## Aggregation Functions

To apply SQL functions, use the pattern, use the pattern:

    SELECT function_name(amount) FROM babynams WHERE ...;

For `function_name`, insert any of the following:

* `count`
* `sum`
* `min`
* `max`
* `avg`
* `std`

Calculate the total number of babies born in 2021, i.e. the sum of the third column.

Display the number of rows and columns.

Calculate the percentage of girls and boys among the total births.

but calculate the sum for boys and girls separately.


Task 3
------

Calculate the total number of births for each year.


Task 6
------

Finally, we will normalize the data. Repeat Task 4 or 5, but divide the
count of a given name by the total number of births **of that year**.

How does the result change and why is this important?


## Elementary Patterns

Here are more complex queries for frequently used metrics:

### Union

The following query connects the result from two queries in one table.
Not that the parentheses are important and both results need to have the same columns.

    (SELECT name, year, amount FROM babynames WHERE name='Hermione' LIMIT 5)
    UNION
    (SELECT name, year, amount FROM babynames WHERE name='Harry' LIMIT 5);

Create a table that contains the top 5 girls names and top 5 boys names.



### Percentage

    SELECT name, amount,
           amount * 100.0 / (SELECT sum(amount) FROM babynames WHERE year=2009) AS percentage
    FROM babynames
    WHERE year=2009 LIMIT 5;

Use the `sum()` function to check whether the percentages sum up to 100%?

Why does the `WHERE` clause occur twice? What happens if you leave out one or the other.

### Sampling

The following query generates ten random names for undecided parents:

    SELECT name FROM babynames ORDER BY RAND() LIMIT 10;

However, the query can be slow. Here is a faster alternative 

    SELECT name FROM babynames WHERE RAND() <= 0.001 LIMIT 10;

Discuss the difference between both queries.

Note tht in Spark SQL there is a faster variant of the first query:

    SELECT * FROM babynames TABLESAMPLE (10 ROWS);

### Binning

The following query calculates four buckets with an equal number of data points (quartiles):

    WITH quartiles AS (
        SELECT 
            amount,
            NTILE(4) OVER (ORDER BY amount) AS quartile
        FROM babynames
        WHERE year = 2023
    )
    SELECT
        quartile,
        MIN(amount) AS min_value,
        MAX(amount) AS max_value
    FROM quartiles
    GROUP BY quartile
    ORDER BY quartile;

Modify the query to calculate a) 10 buckets b) the median number of births.
