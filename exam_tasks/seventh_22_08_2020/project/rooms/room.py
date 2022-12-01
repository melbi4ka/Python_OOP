from project.appliances.appliance import Appliance
from project.people.child import Child


class Room:

    def __init__(self, name: str, budget: float, members_count: int):

        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.expenses = 0

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self.__expenses = value


    def calculate_expenses(self, *args):
        total_cost_per_all_days = 0
        for el in args:
            for e in el:
                if isinstance(e, Appliance):
                    total_cost_per_all_days += e.get_monthly_expense()
                if isinstance(e, Child):
                    total_cost_per_all_days += e.cost * 30
        self.expenses = total_cost_per_all_days



