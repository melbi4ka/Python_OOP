from project.supply.supply import Supply

class Food(Supply):

    def __init__(self, name, energy=25):
        super().__init__(name, energy)

    def details(self):
        return f"{self.__class__.__name__}: {self.name}, {self.energy}"


f1 = Food("aa", 5)
print(f1.details())