from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.core.austronaut_made import AustronautMade
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository



class SpaceStation:

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.austronaut_made = AustronautMade()
        self.__compleate_missions = 0
        self.__noncompleated_missions = 0

    def add_astronaut(self, astronaut_type: str, name: str):
        if self.astronaut_repository.find_by_name(name):
            return f"{name} is already added."
        astro = self.austronaut_made.create_astronaut(astronaut_type, name)
        self.astronaut_repository.add(astro)
        return f"Successfully added {astro.__class__.__name__}: {name}."

    # @staticmethod
    # def __create_astro(astronaut_type, name):
    #     astro = None
    #     if Biologist.__name__ == astronaut_type:
    #         astro = Biologist(name)
    #     elif Geodesist.__name__ == astronaut_type:
    #         astro = Geodesist(name)
    #     elif Meteorologist.__name__ == astronaut_type:
    #         astro = Meteorologist(name)
    #     if astro is None:
    #         raise Exception("Astronaut type is not valid!")
    #     else:
    #         return astro
    #
    # def add_astronaut(self, astronaut_type: str, name: str):
    #     if any(astro.name == name for astro in self.astronaut_repository.astronauts):
    #         return f"{name} is already added."
    #     astro = self.__create_astro(astronaut_type, name)
    #     self.astronaut_repository.add(astro)
    #     return f"Successfully added {astro.__class__.__name__}: {name}."

    # def add_planet(self, name: str, items: str):
    #     if any(pl.name == name for pl in self.planet_repository.planets):
    #         return f"{name} is already added."
    #     planet = Planet.made_planet(name, items)
    #     self.planet_repository.planets.append(planet)
    #     return f"Successfully added Planet: {name}."
    def add_planet(self, name: str, items: str):
        if self.planet_repository.find_by_name(name):
            return f'{name} is already added.'

        planet = Planet(name)
        planet.items = items.split(', ')
        self.planet_repository.add(planet)

        return f'Successfully added Planet: {name}.'

    def retire_astronaut(self, name: str):
        for astro in self.astronaut_repository.astronauts:
            if astro.name == name:
                self.astronaut_repository.remove(astro)
                # self.astronaut_repository.astronauts.remove(astro)
                return f"Astronaut {name} was retired!"
        raise Exception(f"Astronaut {name} doesn't exist!")

    def recharge_oxygen(self):
        for astro in self.astronaut_repository.astronauts:
            astro.increase_oxygen(10)

    def __if_planet_exist(self, planet_name):
        if all(planet.name != planet_name for planet in self.planet_repository.planets):
            raise Exception("Invalid planet name!")
        for planet in self.planet_repository.planets:
            if planet.name == planet_name:
                return planet

    def __choose_astronauts(self):
        sorted_astro = sorted(self.astronaut_repository.astronauts, key=lambda x: -x.oxygen)
        astro_with_oxygen = []
        for astro in sorted_astro[:5]:
            if astro.oxygen > 30:
                astro_with_oxygen.append(astro)

        if not astro_with_oxygen:
            raise Exception("You need at least one astronaut to explore the planet!")
        return astro_with_oxygen

    @staticmethod
    def __collect_items(missioners, planet):
        participated = 0
        for missioner in missioners:
            if not planet.items:
                break
            while missioner.oxygen > 0 and len(planet.items) > 0:
                missioner.backpack.append(planet.items[-1])
                planet.items.pop()
                missioner.breathe()
            participated += 1
        return planet.items, participated

    def send_on_mission(self, planet_name):
        planet = self.__if_planet_exist(planet_name)
        astro_missioners = self.__choose_astronauts()
        planet_items, participated = self.__collect_items(astro_missioners, planet)
        if not planet_items:
            self.__compleate_missions += 1
            return f"Planet: {planet.name} was explored. {participated} " \
                   f"astronauts participated in collecting items."
        else:
            self.__noncompleated_missions += 1
            return f"Mission is not completed."

    # def send_on_mission(self, planet_name: str):
    #     planet = self.planet_repository.find_by_name(planet_name)
    #
    #     if planet is None:
    #         raise Exception('Invalid planet name!')
    #
    #     astronauts = self.astronaut_repository.find_astronauts_for_mission(5, 30)
    #
    #     if len(astronauts) == 0:
    #         raise Exception('You need at least one astronaut to explore the planet!')
    #
    #     participated_astronauts = 0
    #
    #     for astronaut in astronauts:
    #         if len(planet.items) == 0:
    #             break
    #         while astronaut.oxygen > 0 and len(planet.items) > 0:
    #             astronaut.backpack.append(planet.items.pop())
    #             astronaut.breathe()
    #         participated_astronauts += 1
    #
    #     if len(planet.items) == 0:
    #         self.__compleate_missions += 1
    #         return f'Planet: {planet_name} was explored. {participated_astronauts} astronauts participated in collecting items.'
    #     else:
    #         self.__noncompleated_missions += 1
    #         return f'Mission is not completed.'

    def report(self):
        result = [f"{self.__compleate_missions} successful missions!",
                  f"{self.__noncompleated_missions} missions were not completed!", "Astronauts' info:"]
        for astro in self.astronaut_repository.astronauts:
            result.append(f"Name: {astro.name}")
            result.append(f"Oxygen: {astro.oxygen}")
            if astro.backpack:
                res = f"Backpack items: {', '.join(astro.backpack)}"
                result.append(res)
            else:
                result.append(f"Backpack items: none")

        return "\n".join(result)
