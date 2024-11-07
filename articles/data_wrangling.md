
# Data Wrangling

Load Titanic Dataset

### Exercise 1: First name

Write a query that shows the first name of each passenger
(the first word in the name).

.. seealso::

   Use the `list of MySQL functions <https://www.w3schools.com/sql/sql_ref_mysql.asp>`__

### Exercise 2: DISTINCT

Find all unique ports of embarkment.
Write a query using the keyword `DISTINCT`.

### Exercise 3: Remove missing values

Modify the following query to not show the passengers with missing age.

::

    SELECT name, age, age IS NULL FROM titanic;

### Exercise 4: Complete Missing age

Calculate the median age. Then write a query that reports complete ages.
If the age is not present, use the median instead.

Use the CASE statement.

### Exercise 5: Type conversion

Find a functiont that converts the type of the `age` column to a string so that
you can create a query attaching the word **years**, e.g.:

::
 
    Rose | 24 years
    Jack | 26 years

### Exercise 6: Combined columns

Create a SELECT query that produces:

* a column containing 'child' or 'adult'.
* a column containing a label like `male_1st_class`
