from abc import ABC, abstractmethod

from project.core.validator import Validator


class BaseAquarium(ABC):

    @abstractmethod
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_if_string_is_empty_or_whitespace(value, "Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        return sum([decoration.comfort for decoration in self.decorations])

    def add_fish(self, fish):
        fish_types = ["FreshwaterFish", "SaltwaterFish"]
        if self.capacity == len(self.fish):
            return f"Not enough capacity."

        if fish.__class__.__name__ in fish_types:
            self.fish.append(fish)
            return f"Successfully added {fish.__class__.__name__} to {self.name}."


    def remove_fish(self, fish):
        self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):

        result = [f"{self.name}:"]
        if len(self.fish) > 0:
            result.append(f"Fish: {' '.join([fish.name for fish in self.fish])}")
        else:
            result.append("Fish: none")
        result.append(f"Decorations: {len(self.decorations)}")
        result.append(f"Comfort: {self.calculate_comfort()}")

        return "\n".join(result)
