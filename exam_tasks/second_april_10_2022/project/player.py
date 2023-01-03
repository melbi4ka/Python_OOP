class Player:
    player_names = []

    def __init__(self, name, age, stamina=100):
        self.name = name
        self.age = age
        self.stamina = stamina
        self.__need_sustenance = False

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name not valid!")
        if value not in Player.player_names:
            Player.player_names.append(value)
        else:
            raise Exception(f"Name {value} is already used!")
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 12:
            raise ValueError("The player cannot be under 12 years old!")
        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        if 0 <= value <= 100:
            self.__stamina = value
        else:
            raise ValueError("Stamina not valid!")
        
    @property
    def need_sustenance(self):
        return self.stamina < 100
    # if not work properly check self.__stamina

    def increase_stamina(self, supply):
        if self.stamina + supply.energy > 100:
            self.stamina = 100
        else:
            self.stamina += supply.energy


    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"
