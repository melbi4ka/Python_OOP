from project.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):

    # def __init__(self, name):
    #     super().__init__(name, oxygen = 50)

    def __init__(self, name, oxygen = 50):
        super().__init__(name, oxygen)

    def breathe(self):
        self.oxygen -= 10

#     def __str__(self):
#         return f"{self.name}{self.oxygen}"
#
#
# g = Geodesist("Neil")
# print(g)