class Player:

    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = "Unaffiliated"
        self.default_guild = "Unaffiliated"

    def add_skill(self, skill_name, mana_cost):
        if skill_name in self.skills:
            return f"Skill already added"
        self.skills[skill_name] = mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self):
        x = "\n"
        result = f"Name: {self.name}{x}" \
                 f"Guild: {self.guild}{x}" \
                 f"HP: {self.hp}{x}" \
                 f"MP: {self.mp}{x}"
        for skill_name, mana_cost in self.skills.items():
            result += f"==={skill_name} - {mana_cost}"
            result += x
        return result


