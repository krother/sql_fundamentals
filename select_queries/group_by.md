
## Aggregation Functions

In this section, you will explore one of the most powerful concepts in SQL: Aggregation.

### Exercise 1: Simple Aggregation

To apply aggregation functions in SQL, use the pattern:

    SELECT function_name(births) FROM babynames WHERE ...;

For `function_name`, insert any of the following:

* `count`
* `sum`
* `min`
* `max`
* `avg`
* `std`

Calculate the total number of babies born in 2021, i.e. the sum of the third column.

### Exercise 2: Count rows

Display the total number of rows.

### Exercise 3: Percentage

Calculate the percentage of girls among the total births.

You will need to execute two queries in total.
Apply arithmetics and insert the number of total births from the first query manually.

### Exercise 4: GROUP BY

Aggregation becomes more powerful with the GROUP BY statement.
To calculate the sum of boys and girls in one query, type:

    SELECT gender, sum(births)
      FROM babynames
      GROUP BY gender;

How does the pattern change?

### Exercise 5: Filter before grouping

Add a `WHERE` statement before the `GROUP BY` to narrow down the result to the year 2023.


### Exercise 6: Yearly totals

Calculate the total number of births for each year.

### Exercise 7: Debug

Fix two bugs in the following query:

    SELECT name, births FROM babynames
        GROUP BY name
        WHERE gender = 'F';

### Exercise 8: HAVING

Run the following two queries and explain the difference:

    SELECT name, sum(births) FROM babynames
        WHERE births > 20000
        GROUP BY name;

and

    SELECT name, sum(births) FROM babynames
        GROUP BY name
        HAVING sum(births) > 20000;
