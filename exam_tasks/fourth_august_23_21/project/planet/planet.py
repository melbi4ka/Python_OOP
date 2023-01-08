class Planet:

    def __init__(self, name):
        self.name = name
        self.items = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value or value.isspace():
            raise ValueError("Planet name cannot be empty string or whitespace!")
        self.__name = value

    @staticmethod
    def made_planet(name, items):
        new_planet = Planet(name)
        items_as_list = items.split(", ")
        for item in items_as_list:
            new_planet.items.append(item)
        return new_planet

#     def __str__(self):
#         return f"{self.name}{self.items}"
#
#
# p = Planet("a")
# print(p)
# print(p.made_planet("jupi", "water, beer, wine, soil"))
