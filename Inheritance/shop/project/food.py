from project.product import Product


class Food(Product):
    DEFAULT_QUANTITY = 15

    def __init__(self, name):
        super().__init__(name, self.DEFAULT_QUANTITY)



# това е другия начин да сетнем количеството за класа
# като го направим равно на константа през инстанцията
