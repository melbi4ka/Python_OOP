from project.core.add_aquaruim import CreateAquarium
from project.core.add_decoration import CreateDecoration
from project.core.add_fish import CreateFish
from project.decoration.decoration_repository import DecorationRepository


class Controller:

    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []


    def __aquarium_by_name(self, aquarium_name):
        for aq in self.aquariums:
            if aq.name == aquarium_name:
                return aq
        return None

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        aquarium = CreateAquarium.create_aquarium(aquarium_type, aquarium_name)
        if aquarium is None:
            return f"Invalid aquarium type."
        self.aquariums.append(aquarium)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        decoration = CreateDecoration.create_decoration(decoration_type)
        if decoration is None:
            return f"Invalid decoration type."
        self.decorations_repository.add(decoration)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        decoration = self.decorations_repository.find_by_type(decoration_type)
        aquarium = self.__aquarium_by_name(aquarium_name)
        if decoration == "None":
            return f"There isn't a decoration of type {decoration_type}."
        if aquarium is None:
            return
        self.decorations_repository.remove(decoration)
        aquarium.add_decoration(decoration)
        return f"Successfully added {decoration_type} to {aquarium_name}."

    # no points

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        fish = CreateFish.create_fish(fish_type, fish_name, fish_species, price)
        aquarium = self.__aquarium_by_name(aquarium_name)
        if fish is None:
            return f"There isn't a fish of type {fish_type}."

        if fish_type == "FreshwaterFish":
            if aquarium.__class__.__name__ != "FreshwaterAquarium":
                return "Water not suitable."
        elif fish_type == "SaltwaterFish":
            if aquarium.__class__.__name__ != "SaltwaterAquarium":
                return "Water not suitable."
        result = aquarium.add_fish(fish)
        return result

    def feed_fish(self, aquarium_name: str):
        aquarium = self.__aquarium_by_name(aquarium_name)
        aquarium.feed()
        return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name: str):
        aquarium = self.__aquarium_by_name(aquarium_name)
        res = 0
        for decoration in aquarium.decorations:
            res += decoration.price
        for fish in aquarium.fish:
            res += fish.price
        return f"The value of Aquarium {aquarium_name} is {res:.2f}."

    def report(self):
        result = []
        for aquarium in self.aquariums:
            result.append(str(aquarium))
        return "\n".join(result)
