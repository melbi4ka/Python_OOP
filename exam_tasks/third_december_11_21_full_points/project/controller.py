from project.core import CarFactory
from project.driver import Driver
from project.race import Race


class Controller:

    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []
        self.car_factory = CarFactory()

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if any(car.model == model for car in self.cars):
            raise Exception(f"Car {model} is already created!")
        try:
            car = self.car_factory.create_car(car_type, model, speed_limit)
            self.cars.append(car)
            return f"{car.__class__.__name__} {model} is created."
        except ValueError:
            pass


    def create_driver(self, driver_name: str):
        if any(driver.name == driver_name for driver in self.drivers):
            raise Exception(f"Driver {driver_name} is already created!")
        current_driver = Driver(driver_name)
        self.drivers.append(current_driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        if any(race.name == race_name for race in self.races):
            raise Exception(f"Race {race_name} is already created!")
        current_race = Race(race_name)
        self.races.append(current_race)
        return f"Race {race_name} is created."

    def driver_exist(self, driver_name):
        for dr in self.drivers:
            if dr.name == driver_name:
                return dr
        raise Exception(f"Driver {driver_name} could not be found!")

    def last_car_exist(self, car_type):
        for car in self.cars[::-1]:
            if not car.is_taken and car.__class__.__name__ == car_type:
                return car
        raise Exception(f"Car {car_type} could not be found!")

    def add_car_to_driver(self, driver_name: str, car_type: str):
        current_driver = self.driver_exist(driver_name)
        driver_car = self.last_car_exist(car_type)
        if current_driver.car is None:
            current_driver.car = driver_car
            current_driver.car.is_taken = True
            return f"Driver {driver_name} chose the car {driver_car.model}."
        else:
            current_driver.car.is_taken = False
            old_model = current_driver.car.model
            current_driver.car = driver_car
            current_driver.car.is_taken = True
            return f"Driver {driver_name} changed his car from {old_model} to {driver_car.model}."

    def race_exist(self, race_name):
        for race in self.races:
            if race.name == race_name:
                return race
        raise Exception(f"Race {race_name} could not be found!")

    def add_driver_to_race(self, race_name: str, driver_name: str):
        current_race = self.race_exist(race_name)
        current_driver = self.driver_exist(driver_name)
        if current_driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        for dr in current_race.drivers:
            if dr.name == current_driver.name:
                return f"Driver {driver_name} is already added in {race_name} race."

        current_race.drivers.append(current_driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        current_race = self.race_exist(race_name)
        if len(current_race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")
        sorted_drivers = sorted(current_race.drivers, key=lambda x: -x.car.speed_limit)
        result = []
        for drv in sorted_drivers[:3]:
            drv.number_of_wins += 1
            result.append(f"Driver {drv.name} wins the {race_name} race "
                          f"with a speed of {drv.car.speed_limit}.")
        return "\n".join(result)
