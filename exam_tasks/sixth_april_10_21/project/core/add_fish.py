from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class CreateFish:

    @staticmethod
    def create_fish(fish_type: str, fish_name: str, fish_species: str, price: float):
        if fish_type == "FreshwaterFish":
            return FreshwaterFish(fish_name, fish_species, price)
        if fish_type == "SaltwaterFish":
            return SaltwaterFish(fish_name, fish_species, price)
        return None
    
