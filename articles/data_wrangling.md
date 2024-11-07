
# Data Wrangling

### Space Titanic

In this exercise we will use an excerpt of the `Kaggle Spaceship Titanic Dataset [www.kaggle.com/competitions/spaceship-titanic](https://www.kaggle.com/competitions/spaceship-titanic)
On the server, load it to the database with:

   wget https://github.com/krother/sql_fundamentals/raw/refs/heads/main/data/space_titanic.sql
   mycli < space_titanic.sql

   mycli


### Exercise 1: First name

Write a query that shows the first name of each passenger
(the first word in the name).

Use the `list of MySQL functions [www.w3schools.com/sql/sql_ref_mysql.asp](https://www.w3schools.com/sql/sql_ref_mysql.asp)

### Exercise 2: DISTINCT

Find all unique ports of embarkment.
Write a query using the keyword `DISTINCT`.

### Exercise 3: Identify missing values

Display the passengers for whom the information about the shopping mall is unknown:

    SELECT name, shopping_mall, shopping_mall IS NULL FROM titanic;

The resulting integer is also called a **dummy column**.

### Exercise 4: Remove missing values

Modify the previous query to **not** show passengers with missing age.

### Exercise 5: Complete Missing age

Calculate the median age. Then write a query that reports complete ages.
If the age is not present, use the median instead.

You will need to use a CASE statement. Here is an example:

    SELECT name, shopping_mall, 
          CASE 
              WHEN shopping_mall IS NULL THEN 'bad' 
              ELSE 'good'
          END AS data_quality
    FROM titanic LIMIT 20;

### Exercise 6: Type conversion

Find a functiont that converts the type of the `age` column to a string so that
you can create a query attaching the word **years**, e.g.:

 
    Rose | 24 years
    Jack | 26 years

### Exercise 7: Combined columns

Create a SELECT query that produces:

* a column containing 'child' or 'adult'.
* a column containing a label like `male_1st_class`
