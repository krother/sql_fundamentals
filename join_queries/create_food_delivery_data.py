import random
import uuid
from faker import Faker

fake = Faker()

PCS = ["carrot", "tomato", "cucumber", "zucchini", "cauliflower", "eggplant", "weisswurst"]
G = ["flour", "cream", "basil", "beans", "lentils", "parsley", "chickpeas", "potatos", "basmati rice", "parmiggiano", "mozzarella", "wild rice", "jasmine rice", "tagliatelle", "fettuccini", "pak choi"]

INGREDIENT_NAMES = PCS + G
UNITS = ["pcs"] * len(PCS) + ["g"] * len(G)

SUPPLIERS = [fake.company() for _ in range(12)]

def generate_ingredients():
    ingredients = []
    for i, (name, unit) in enumerate(zip(INGREDIENT_NAMES, UNITS)):
        ingredients.append({
            'id': 1000 + i,
            'name': name,
            'uuid': str(uuid.uuid4()),
            'unit': unit,
        })
    return ingredients


def generate_recipes():
    recipes = []
    for i in range(50):
        rtype = random.choice(["Curry", "Stew", "Eintopf", "Creme", "Shakshuka", "Soup", "Pan", "Ratatouille", "Menu"])
        r = random.randint(1, 4) 
        if r == 1:
            name = fake.last_name() + "'s " + rtype
        elif r == 2:
            name = rtype + " " + fake.city() + " Style"
        elif r == 3:
            name = rtype + " a la " + fake.first_name()
        else:
            name = fake.country() + " " + rtype
        recipes.append({
            'id': i + 1,
            'name': name,
        })
    return recipes


def generate_recipe_ingredients(recipes, ingredients):
    result = []
    for r in recipes:
        n = random.randint(3, 8)
        s = set()
        while len(s) < n:
            ing = random.choice(ingredients)
            if ing["id"] not in s:
                s.add(ing["id"])
                result.append((r['id'], ing['id']))
                print(f"INSERT INTO recipe_ingredient (recipe_id, ingredient_id) VALUES ({r['id']}, '{ing['id']}');")
    return result


def generate_addresses():
    addresses = []
    for _ in range(100):
        addresses.append({
            'name': fake.name(),
            'street': fake.street_address(),
            'postal_code': fake.postcode()
        })
    return addresses


def generate_customers(addresses):
    customers = []
    for i in range(100):
        customers.append({
            'address_id': addresses[i]['id']
        })
    return customers


def generate_ingredient_batches(ingredients):
    ingredient_batches = []
    i = 1
    for ing in ingredients:
        for _ in range(random.randint(1, 10)):
            ingredient_batches.append({
                'id': i,
                'ingredient_id': ing['id'],
                'delivery_date': fake.date_this_year(),
                'expiry_date': fake.date_this_year(),
                'amount': random.randint(1, 100),
                'supplier': random.choice(SUPPLIERS)
            })
            i += 1
    return ingredient_batches


def generate_deliveries(customers, recipes, rec_ing, ingredient_batches):
    deliveries = []
    for i in range(200):
        rec = random.choice(recipes)
        for rec_id, ing_id in rec_ing:
            if rec_id == rec["id"]:
                batch = None
                while batch is None:
                    b = random.choice(ingredient_batches)
                    if b["ingredient_id"] == ing_id:
                        batch = b["id"]
        deliveries.append({
            'id': i + 1,
            'customer_id': random.choice(customers)['id'],
            'recipe_id': rec_id,
            'ingredient_batch_id': batch,
            'delivery_date': fake.date_this_year()
        })
    return deliveries


# Generate ingredients
ingredients = generate_ingredients()
for ingredient in ingredients:
    print(f"INSERT INTO ingredient (id, name, uuid, unit) VALUES ({ingredient['id']}, '{ingredient['name']}', '{ingredient['uuid']}', '{ingredient['unit']}');")

# Generate addresses
addresses = generate_addresses()
for i, address in enumerate(addresses):
    address['id'] = i + 1  # Simulate autoincrement id
    print(f"INSERT INTO address (id, name, street, postal_code) VALUES ({address['id']}, '{address['name']}', '{address['street']}', '{address['postal_code']}');")

# Generate customers
customers = generate_customers(addresses)
for i, customer in enumerate(customers):
    customer['id'] = i + 1  # Simulate autoincrement id
    print(f"INSERT INTO customer (id, address_id) VALUES ({customer['id']}, {customer['address_id']});")

# Generate recipes
recipes = generate_recipes()
for i, recipe in enumerate(recipes):
    recipe['id'] = i + 1  # Simulate autoincrement id
    print(f"INSERT INTO recipe (id, name) VALUES ({recipe['id']}, '{recipe['name']}');")

rec_ing = generate_recipe_ingredients(recipes, ingredients)

# Generate ingredient batches
ingredient_batches = generate_ingredient_batches(ingredients)
for i, batch in enumerate(ingredient_batches):
    batch['id'] = i + 1  # Simulate autoincrement id
    print(f"INSERT INTO ingredient_batch (id, ingredient_id, delivery_date, expiry_date, amount, supplier) "
            f"VALUES ({batch['id']}, {batch['ingredient_id']}, '{batch['delivery_date']}', '{batch['expiry_date']}', {batch['amount']}, '{batch['supplier']}');")

# Generate deliveries
deliveries = generate_deliveries(customers, recipes, rec_ing, ingredient_batches)
for delivery in deliveries:
    print(f"INSERT INTO delivery (id, customer_id, recipe_id, ingredient_batch_id, delivery_date) "
            f"VALUES ({delivery['id']}, {delivery['customer_id']}, {delivery['recipe_id']}, {delivery['ingredient_batch_id']}, '{delivery['delivery_date']}');")

