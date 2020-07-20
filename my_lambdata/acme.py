import random


class Product:
    """Class to set Product default attributes
    """

    def __init__(self, name, price=10, weight=20, flammability=0.5,
                 identifier=random.randint(1000000, 9999999)):

        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        """Prints the product's stealablility"""

        if self.weight / self.price < 0.5:
            print("'Not so stealable...'")
            return
        elif self.weight / self.price >= 0.5 < 1.0:
            print("'Kinda stealable.'")
            return
        else:
            print("'Very stealable!'")
            return

    def explode(self):
        """Prints that happen if the product is too flammable"""

        if self.weight * self.flammability < 10:
            print("'...fizzle'")
            return
        elif self.weight * self.flammability >= 10 < 50:
            print("'...boom!'")
            return
        else:
            print("'...BABOOM!!'")
            return
        pass


class BoxingGlove(Product):
    """Class to set Boxing glove parameters.
    """
    def __init__(self, price=10):
        super().__init__(price)

    def explode(self):
        """Prints that will happen if the product is too flammable"""
        print("""\"...it's a glove.\"""")

    def punch(self):
        """Prints that happen when boxing glove punches someone."""
        if self.weight < 5:
            print("'tickles.'")
            return
        elif self.weight >= 5 < 15:
            print("'hurt'")
            return
        else:
            print('\"OUCH!\"')
            return
    pass
        pip install -i https://test.pypi.org/simple/ lambdata-rokshanaparul