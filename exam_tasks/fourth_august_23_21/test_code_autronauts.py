from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.space_station import SpaceStation

b = Biologist("Mike")
g = Geodesist("Peter")
m = Meteorologist("George")
p = Planet("Mars")
ss = SpaceStation()
print(ss.add_astronaut("Biologist", "Neil"))
print(ss.add_astronaut("Geodesist", "Tom"))
print(ss.add_astronaut("Biologist", "Neil"))
print(ss.add_astronaut("Meteorologist", "Elvis"))
# print(ss.add_astronaut("Meteo", "Elvi"))
print(ss.add_planet("Mars", "water, soil, copper, beer, metals, silicone, a, b, c, d, e, f"))
print(ss.add_planet("Mars", "water, soil, copper, beer"))
print(ss.add_planet("Jupi", "water, soil, copper, beer"))
print(ss.planet_repository.planets[0].items)
ss.recharge_oxygen()
print(ss.astronaut_repository.astronauts[0].oxygen)
print(ss.retire_astronaut("Tom"))
print(ss.add_astronaut("Geodesist", "Tom"))
# print(ss.retire_astronaut("Svetlana"))
# print(ss.send_on_mission("R2D2"))
for _ in range(6):
    ss.astronaut_repository.astronauts[0].breathe()

print(ss.astronaut_repository.astronauts[0].oxygen)
# ss.astronaut_repository.astronauts[2].breathe()
ss.astronaut_repository.astronauts[2].breathe()
# ss.astronaut_repository.astronauts[2].breathe()
print(ss.astronaut_repository.astronauts[2].oxygen)
print(ss.report())
print(ss.send_on_mission("Mars"))
print(ss.report())
#
#
