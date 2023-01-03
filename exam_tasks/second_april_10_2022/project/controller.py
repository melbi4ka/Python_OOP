from project import player
from project.supply.drink import Drink
from project.supply.food import Food


class Controller:

    def __init__(self):
        self.players = []
        self.supplies = []

    # def add_player(self, *players):
    #     players_to_add = [player for player in players if player not in self.players]
    #     self.players += players_to_add
    #     return f"Successfully added: {', '.join(player.name for player in players_to_add)}"

    def add_player(self, *players):
        added = []
        for plr in players:
            if plr not in self.players:
                self.players.append(plr)
                added.append(plr)
        return f"Successfully added: {', '.join(pl.name for pl in added)}"

    def add_supply(self, *supplies):
        for spl in supplies:
            self.supplies.append(spl)

    def player_in_list(self, player_name):
        if all(pl.name != player_name for pl in self.players):
            return False
        return True

    def player_by_name(self, player_name):
        for pl in self.players:
            if pl.name == player_name:
                return pl

    def sustain(self, player_name, sustenance_type):
        if self.player_in_list(player_name):
            for idx in range(len(self.supplies) - 1, -1, -1):
                current = self.supplies[idx]
                if current.__class__.__name__ == sustenance_type:
                    pl = self.player_by_name(player_name)
                    if pl.stamina == 100:
                        return f"{player_name} have enough stamina."
                    pl.increase_stamina(current)
                    self.supplies.pop(idx)
                    return f"{player_name} sustained successfully with {current.name}."
            if sustenance_type == "Food":
                raise Exception("There are no food supplies left!")
            if sustenance_type == "Drink":
                raise Exception("There are no drink supplies left!")

    @staticmethod
    def attack(pl_one, pl_two):
        pl_two.stamina -= (pl_one.stamina / 2)
        if pl_one.stamina - (pl_two.stamina / 2) < 0:
            pl_one.stamina = 0
        else:
            pl_one.stamina -= (pl_two.stamina / 2)
        if pl_one.stamina < pl_two.stamina:
            return f"Winner: {pl_two.name}"
        else:
            return f"Winner: {pl_one.name}"

    def duel(self, first_player_name, second_player_name):
        pl_one = self.player_by_name(first_player_name)
        pl_two = self.player_by_name(second_player_name)
        result = []

        if pl_one.stamina == 0:
            result.append(f"Player {pl_one.name} does not have enough stamina.")
        if pl_two.stamina == 0:
            result.append(f"Player {pl_two.name} does not have enough stamina.")
        if result:
            return "\n".join(result)

        if pl_one.stamina < pl_two.stamina:
            return self.attack(pl_one, pl_two)
        else:
            return self.attack(pl_two, pl_one)

    def next_day(self):

        for p in self.players:
            if p.stamina - (p.age * 2) < 0:
                p.stamina = 0
            else:
                p.stamina -= (p.age * 2)
        for pl in self.players:
            self.sustain(pl.name, "Food")
            self.sustain(pl.name, "Drink")

    def __str__(self):
        result = []

        for pl in self.players:
            result.append(str(pl))

        for spl in self.supplies:
            result.append(spl.details())

        return "\n".join(result)
