from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):

    # def __init__(self, name):
    #     super().__init__(name, oxygen = 70)

    def __init__(self, name, oxygen = 70):
        super().__init__(name, oxygen)

    def breathe(self):
        self.oxygen -= 5

#     def __str__(self):
#         return f"{self.name}{self.oxygen}"
#
#
# b = Biologist("Neil")
# # b.oxygen = 100
# print(b)
