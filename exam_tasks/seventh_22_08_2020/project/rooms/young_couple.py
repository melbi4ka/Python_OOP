from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.stove import Stove
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCouple(Room):

    def __init__(self, family_name: str, salary_one: float, salary_two: float):
        super().__init__(family_name, salary_one + salary_two, 2)
        self.room_cost = 20
        self.appliances = [TV(), Fridge(), Laptop()] * 2
        self.calculate_expenses(self.appliances)

    # def calcululate_apliances(self):
    #     result = 0
    #     for el in self.appliances:
    #         result += el.get_monthly_expense()
    #     return result
    # def calculate_appliances(self):
    #     super().calculate_expenses()