
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist


class AustronautMade:

    austronaut_types = {"Biologist" : Biologist,
                 "Geodesist": Geodesist,
                 "Meteorologist": Meteorologist
                 }

    def create_astronaut(self, astronaut_type: str, name: str):
        if astronaut_type not in self.austronaut_types:
            raise Exception("Astronaut type is not valid!")
        return self.austronaut_types[astronaut_type](name)
