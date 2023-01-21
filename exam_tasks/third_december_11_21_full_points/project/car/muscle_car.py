from project.car.car import Car


class MuscleCar(Car):
    # MIN_SPEED_LIMIT = 250
    # MAX_SPEED_LIMIT = 450

    def __init__(self, model, speed_limit):
        super().__init__(model, speed_limit)


    @property
    def min_speed_limit(self):
        return 250

    @property
    def max_speed_limit(self):
        return 450


    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value):
        if value < self.min_speed_limit or value > self.max_speed_limit:
            raise ValueError (f"Invalid speed limit! Must be between {self.min_speed_limit} "
                              f"and {self.max_speed_limit}!")
        self.__speed_limit = value

#     def __str__(self):
#         return f"{self.model} {self.speed_limit}"
#
#
# mc = MuscleCar("aaaaa", 700)
# print(mc)
