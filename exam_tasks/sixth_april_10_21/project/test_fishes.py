from project.controller import Controller

cll = Controller()
print(cll.add_aquarium("FreshwaterAquarium", "Roza"))
print(cll.add_aquarium("FreshwaterAquariumsss", "Roza"))
print(cll.add_aquarium("FreshwaterAquarium", "Zizu"))
print(cll.add_decoration("Ornament"))
print(cll.add_decoration("Plant"))
print(cll.add_decoration("Ornament"))
print(cll.add_decoration("Ornamentssss"))
print(cll.insert_decoration("Roza", "Ornament"))
print(cll.insert_decoration("Roza", "Ornamentssss"))
print(cll.decorations_repository.decorations[0].__class__.__name__)
print(cll.decorations_repository.decorations[1].__class__.__name__)
print(cll.add_fish("Roza","FreshwaterFish", "Ab", "Cd", 1.50))
print(cll.add_fish("Roza","FreshwaterFish", "Ac", "Dc", 2.50))
print(cll.add_fish("Roza","SaltwaterFishhhh", "Ac", "Dc", 2.50))
print(cll.add_fish("Roza","SaltwaterFish", "Ac", "Dc", 2.50))
print(cll.feed_fish("Roza"))
print(cll.calculate_value("Roza"))
print(cll.report())
