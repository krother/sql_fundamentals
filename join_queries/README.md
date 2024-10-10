
# Session 2: Exercises

## Part 1: Explore a  Data Model

### Exercise 1: Log into Workspace and read data

1. Login to [https://workspace.hackschule.de](https://workspace.hackschule.de).
2. In the editor, open a terminal with (**"Terminal -> New Terminal"**) or use an existing one.

Read the data with the commands:

    wget https://raw.githubusercontent.com/krother/sql_fundamentals/refs/heads/main/join_queries/food_delivery_data.sql
    mysql < food_delivery_data.sql
    mycli


### Exercise 2: Explore tables

Check which tables are there by typing:

    SHOW TABLES;

You can see the column definitions of each table with:

    DESCRIBE tablename;

Alternatively, you could open the 

**Discuss what data types you find in the tables. What else do you see?**

Next, let's write a few SQL queries:

### Exercise 3: SELECT

Display the first 10 recipes.

### Exercise 4: count()

How many recipes are there in total?

### Exercise 5: WHERE

How many ingredients are measured in pieces?

### Exercise 6: Date

Which deliveries took place after July 1st?
Use the phrase:

    WHERE delivery_date > '2024-....


### Exercise 7: comparison

Find an ingredient batch with > 90 items of the same ingredient.

### Exercise 8: sum()

How many tomatoes were supplied in all ingredient batches in total?

**Hint:** You may need to run two small queries to answer this question.

### Exercise 9: GROUP BY

Calculate the total amount of each ingredient over all batches.


### Exercise 10: Foreign Keys

Look at the **id** columns and **other_table_id** columns. 
Which tables are connected to which others.

Open the file `food_delivery_data.sql` in the editor and inspect the `CREATE TABLE` statements.

### Exercise 11: Entity-Relationship Diagram

Draw a diagram that shows the connections between tables.
On [dbdiagram.io](https://dbdiagram.io/) this can be created with the following steps:

1. Copy the complete `CREATE TABLE` statements
2. Go to [dbdiagram.io](https://dbdiagram.io/)
3. Select **import -> MySQL**
4. Paste the SQL code
5. Move around the boxes so that the connections are easy to see

Discuss the **cardinality** of tables. Which connections are:

* one-to-one (1:1)
* one-to-many (1:N)
* many-to-many (N:M)


## Part 2: JOIN Example Queries

### Example 1: INNER JOIN

Execute the following code:
 
    SELECT * FROM customer c
    INNER JOIN address a
    ON c.address_id = a.id;

### Example 2: Remove data
Let's remove some data:

    DELETE FROM address WHERE id BETWEEN 3 AND 8;

and 

    DELETE FROM customer WHERE id BETWEEN 7 AND 12;

Run the previous query again. What do you notice?

### Example 3: LEFT JOIN

Now try:

    SELECT * FROM customer c
    LEFT JOIN address a
    ON c.address_id = a.id;

What does change?

### Example 4: RIGHT JOIN

Try the same with `RIGHT JOIN`.

**Note that there is no `FULL OUTER JOIN` in MySQL. However there might be in your database.**

### Example 5: CROSS JOIN

Create combinations of two ingredients:

    SELECT i1.name, i2.name FROM ingredient i1
    CROSS JOIN ingredient i2;

## Part 3: JOIN Exercises

### Exercise 1

Display all ingredient batches from which a delivery was made to customer 3.

### Exercise 2

Display recipe 5 and all its ingredients.

### Exercise 3

Show all recipes that contain carrots.

### Exercise 4

Find the names of all recipes with 5 or more ingredients.

SELECT
### Exercise 1

Ingredient batch with id 7 was bad. Which customers need to be contacted?

