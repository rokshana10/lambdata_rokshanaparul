# Part 1,2,3
import random 
from acme import Product
from acme import Product, BoxingGlove

# Part 1
class Product():
    def __init__(self, 
                 name, 
                 price = 10, 
                 weight = 20, 
                 flammability = 0.5, 
#                  identifier
                ):
        
        # random from 1000000 to 9999999, includisve
        self.identifier = random.randint(1000000, 9999999)
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
    
    def stealability(self):
        steal = self.price / self.weight
        if steal < 0.5:
            return "Not so stealable..."
        elif (steal >= 0.5) and (steal < 1.0):
            return "Kinda stealable."
        else:
            return "Very stealable!"
    
    def explode(self):
        expl = (self.flammability * self.weight)
        if expl < 10:
            return "...fizzle."
        elif (expl >= 10) and (expl < 50):
            return "...boom!"
        else:
            return "...BABOOM!!"
    
class BoxingGlove(Product):
    def __init__(self, name):
        super().__init__(name, weight=10)
  
    def explode(self):
        return "...it's a glove."
  
    def punch(self):
        if self.weight < 5:
            return "That tickles."
        elif self.weight >= 5 and self.weight < 15:
            return "Hey that hurt!"
        else:
            return "OUCH!"


            prod = Product("A Cool Toy")
    print("prod.identifier", prod.identifier)
    print("prod.name", prod.name)
    print("prod.price", prod.price)
    print("prod.weight", prod.weight)
    print("prod.flammability", prod.flammability)

            prod = Product("A Cool Toy")
    print(prod.stealability())
    print(prod.explode())

            glove = BoxingGlove('Punchy the Third')
    print(glove.price) # 10
    print(glove.weight) # 10
    print(glove.punch())
        
        pip install -i https://test.pypi.org/simple/ lambdata-rokshanaparul