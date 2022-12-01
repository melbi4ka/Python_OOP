from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.stove import Stove
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):

    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children):
        count = 2 + len(children)
        super().__init__(family_name, salary_one + salary_two, count)

        self.room_cost = 30
        self.children = list(children)

        self.appliances = [TV(), Fridge(), Laptop()] * self.members_count
        self.calculate_expenses(self.appliances, self.children)

    # def calcululate_apliances(self):
    #     result = 0
    #     for el in self.appliances:
    #         result += el.get_monthly_expense()
    #     return result
    # def calculate_appliances(self):
    #     super().calculate_expenses(self.children, self.appliances)
