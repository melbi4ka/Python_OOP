from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_consumption = fuel_consumption
        self.fuel_quantity = fuel_quantity

    @abstractmethod
    def drive(self, distance):
        if self.fuel_quantity >= self.fuel_consumption * distance:
            self.fuel_quantity -= self.fuel_consumption * distance
        return self.fuel_quantity

    @abstractmethod
    def refuel(self, fuel):
        self.fuel_quantity += fuel
        return self.fuel_quantity


class Car(Vehicle):

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance):
        self.fuel_consumption += 0.9
        super().drive(distance)

    def refuel(self, fuel):
        super().refuel(fuel)


class Truck(Vehicle):

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance):
        self.fuel_consumption += 1.6
        super().drive(distance)

    def refuel(self, fuel):
        fuel *= 0.95
        super().refuel(fuel)
