from project.appliances.tv import TV
from project.rooms.room import Room


class AloneYoung(Room):

    def __init__(self, family_name: str, salary: float):
        super().__init__(family_name, salary, 1)
        self.room_cost = 10
        self.appliances = [TV()]
        self.calculate_expenses(self.appliances)

    # def calculate_appliances(self):
    #     super().calculate_expenses()
    #     # result = 0
    #     # for tv in self.appliances:
    #     #     result += tv.get_monthly_expense()



