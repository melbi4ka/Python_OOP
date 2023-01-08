from project.planet.planet import Planet


class PlanetRepository:

    def __init__(self):
        self.planets = []

    def add(self, planet: Planet):
        self.planets.append(planet)

    def remove(self, planet: Planet):
        if planet in self.planets:
            self.planets.remove(planet)

    # def remove(self, planet: Planet):
    #     self.planets.remove(planet)

    # if needed - remove if

    def find_by_name(self, name: str):
        for planet in self.planets:
            if planet.name == name:
                return planet