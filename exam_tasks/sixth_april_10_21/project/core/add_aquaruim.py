from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium


class CreateAquarium:

    @staticmethod
    def create_aquarium(aquarium_type, aquarium_name):
        if aquarium_type == "FreshwaterAquarium":
            return FreshwaterAquarium(aquarium_name)
        elif aquarium_type == "SaltwaterAquarium":
            return SaltwaterAquarium(aquarium_name)
        return None


