from project.people.child import Child
from project.rooms.room import Room
from project.rooms.young_couple import YoungCouple
from project.rooms.young_couple_with_children import YoungCoupleWithChildren


class Everland:

    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        result = 0
        for room in self.rooms:
            result += room.expenses
            result += room.room_cost
        return f"Monthly consumption: {result:.2f}$."

    def pay(self):
        result = []
        for room in self.rooms:
            total_cost = room.expenses+room.room_cost
            if total_cost < room.budget:
                result.append(f"{room.family_name} paid {total_cost:.2f}$ and have {room.budget - total_cost:.2f}$ left.")
            else:
                result.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
                self.rooms.remove(room)
        return "\n".join(result)

    def status(self):
        all_people = sum([room.members_count for room in self.rooms])
        result = [f"Total population: {all_people}"]
        for room in self.rooms:
            result.append(f"{room.family_name} with {room.members_count} members. "
                          f"Budget: {room.budget - (room.expenses+room.room_cost):.2f}$, Expenses: {room.expenses:.2f}$")
            if room.children:
                for children in room.children:
                    result.append(f"--- Child {room.children.index(children) + 1} monthly cost: {children.cost * 30:.2f}$")
            if room.appliances:
                result.append(f"--- Appliances monthly cost: {sum([apl.cost for apl in room.appliances]) * 30:.2f}$")
        return "\n".join(result)
