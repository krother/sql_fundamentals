## Elementary Patterns

Here are more complex queries for frequently used metrics:

### Union

The following query connects the result from two queries in one table.
Not that the parentheses are important and both results need to have the same columns.

    (SELECT name, year, births FROM babynames WHERE name='Hermione' LIMIT 5)
    UNION
    (SELECT name, year, births FROM babynames WHERE name='Harry' LIMIT 5);

Create a table that contains the top 5 girls names and top 5 boys names.


### Percentage

Here is a compact pattern 

    SELECT name, births,
           births * 100.0 / (SELECT sum(births) FROM babynames WHERE year=2023) AS percentage
    FROM babynames
    WHERE year=2023 LIMIT 5;

Use the `sum()` function to check whether the percentages sum up to 100%?

Why does the `WHERE` clause occur twice? What happens if you leave out one or the other.

### Sampling

The following query generates ten random names for undecided parents:

    SELECT name FROM babynames ORDER BY RAND() LIMIT 10;

However, the query can be slow. Here is a faster alternative 

    SELECT name FROM babynames WHERE RAND() <= 0.001 LIMIT 10;

Discuss the difference between both queries.

Note that in Spark SQL there is a faster variant of the first query:

    SELECT * FROM babynames TABLESAMPLE (10 ROWS);

### Binning

The following query calculates four buckets with an equal number of data points (quartiles):

    WITH quartiles AS (
        SELECT 
            births,
            NTILE(4) OVER (ORDER BY births) AS quartile
        FROM babynames
        WHERE year = 2023
    )
    SELECT
        quartile,
        MIN(births) AS min_value,
        MAX(births) AS max_value
    FROM quartiles
    GROUP BY quartile
    ORDER BY quartile;

Modify the query to calculate a) 10 buckets b) the median number of births.
