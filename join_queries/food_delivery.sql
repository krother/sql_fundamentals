-- Table for ingredients
CREATE TABLE ingredient (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    uuid VARCHAR(36) UNIQUE,
    unit VARCHAR(50)
);

-- Table for recipes
CREATE TABLE recipe (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

-- Many-to-Many relationship between recipes and ingredients
CREATE TABLE recipe_ingredient (
    recipe_id INT REFERENCES recipe(id) ON DELETE CASCADE,
    ingredient_id INT REFERENCES ingredient(id) ON DELETE CASCADE,
    PRIMARY KEY (recipe_id, ingredient_id)
);

-- Table for addresses
CREATE TABLE address (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    street VARCHAR(255),
    postal_code VARCHAR(20)
);

-- Table for customers
CREATE TABLE customer (
    id SERIAL PRIMARY KEY,
    address_id INT REFERENCES address(id) ON DELETE CASCADE
);

-- Table for ingredient batches
CREATE TABLE ingredient_batch (
    id SERIAL PRIMARY KEY,
    ingredient_id INT REFERENCES ingredient(id) ON DELETE CASCADE,
    delivery_date DATE,
    expiration_date DATE,
    amount INT,
    supplier VARCHAR(255)
);

-- Table for deliveries
CREATE TABLE delivery (
    id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customer(id) ON DELETE CASCADE,
    recipe_id INT REFERENCES recipe(id) ON DELETE CASCADE,
    ingredient_batch_id INT REFERENCES ingredient_batch(id) ON DELETE CASCADE,
    delivery_date DATE
);
