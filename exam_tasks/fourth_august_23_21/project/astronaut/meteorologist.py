from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):

    # def __init__(self, name):
    #     super().__init__(name, oxygen = 90)

    def __init__(self, name, oxygen = 90):
        super().__init__(name, oxygen)

    def breathe(self):
        self.oxygen -= 15
