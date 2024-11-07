
## Debugging Queries with GROUP BY

The `GROUP BY` statement is a bit trickier than the other parts of queries.
Here are a few buggy statements specific for that one.

Fix the syntactic and semantic errors:

### Exercise 1

Total number of boys for each year

    SELECT year, sum(births) FROM babynames GROUP BY year WHERE gender='M';

### Exercise 2

Total number of girls/boys

    SELECT gender, year, sum(births) FROM babynames GROUP BY gender;

### Exercise 3

Number of births for the top name for each year

    SELECT year, max(births) FROM babynames GROUP BY max(births) ORDER BY year DESC;

### Exercise 4

Number of different names for each year/gender combination for each year ending with a zero.

    SELECT year, gender, count(name) FROM babynames WHERE year % 10 = 0;

### Exercise 5

Names with more than 4M births over all the US history

    SELECT name, sum(births) FROM babynames WHERE sum(births) > 4000000 GROUP BY name ORDER BY sum(births) DESC;
