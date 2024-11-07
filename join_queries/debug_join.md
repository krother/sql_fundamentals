
# Debug queries with JOIN

### Example 1

    SELECT * FROM ingredient
       INNER JOIN ingredient_batch
       ON ingredient_id = ingredient_batch_id
       LIMIT 10;

### Example 2

    SELECT * FROM delivery AS d
       WHERE d.ingredient_batch_id=144
       INNER JOIN customer AS c
       ON d.customer_id = c.id
       LIMIT 10;
    
### Example 3
    
    
    SELECT r.recipe_id, i.name FROM recipe_ingredient AS r
       INNER JOIN ingredient AS i
       ON i.id=r.id
       GROUP BY i.name;y
