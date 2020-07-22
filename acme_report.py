import random 
from random import randint, sample, uniform
from acme import Product

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']
    
def generate_products(num_products=30):
    
    products = []
    for _ in range(num_products):
        name = ADJECTIVES[randint(0, 4)] + \
               ' ' + \
               NOUNS[randint(0, 4)]

        price = randint(5, 100)
        weight = randint(5, 100)
        flammability = uniform(0., 2.5)

        prod = Product(name=name, 
                       price=price,
                       weight=weight,
                       flammability=flammability)
        products.append(prod)
    
    return products

def inventory_report(products):
  
    prod_num = len(products)
    if prod_num <= 0:
        return "No products!"
  
    ttl_price, ttl_weight, ttl_flam = 0, 0, 0
    for prod in products:
        ttl_price += prod.price
        ttl_weight += prod.weight
        ttl_flam += prod.flammability
   
    avg_price = ttl_price / prod_num
    avg_weight = ttl_weight / prod_num
    avg_flam = ttl_flam / prod_num
  
    print("ACME CORPORATION OFFICIAL INVENTORY REPORT")
    print("Unique product names:", len(set(products)))
    print("Average price:", avg_price)
    print("Average weight:", avg_weight)
    print("Average flammability:", avg_flam)

if __name__ == '__main__':
pip install -i https://test.pypi.org/simple/ lambdata-rokshanaparul
