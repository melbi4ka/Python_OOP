from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar




class CarFactory:

    car_types = {"SportsCar" : SportsCar,
                 "MuscleCar": MuscleCar
                 }

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type not in self.car_types:
            raise ValueError
        return self.car_types[car_type](model, speed_limit)


        # if any([car.model == model for car in self.cars]):
        #     raise Exception(f"Car {model} is already created!")
        # # for car in self.cars:
        # #     if car.model == model:
        # #         raise Exception (f"Car {model} is already created!")
        # current_car = self.car_type_create(car_type, model, speed_limit)
        # if current_car:
        #     self.cars.append(current_car)
        #     return f"{car_type} {model} is created."