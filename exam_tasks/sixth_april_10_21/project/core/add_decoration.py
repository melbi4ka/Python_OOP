from project.decoration.plant import Plant
from project.main import Ornament


class CreateDecoration:

    @staticmethod
    def create_decoration(decoration_type):
        if decoration_type == "Ornament":
            return Ornament()
        elif decoration_type == "Plant":
            return Plant()
        return None