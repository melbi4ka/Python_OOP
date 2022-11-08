from project import keeper, vet, caretaker, lion, cheetah, tiger
from project.animal import Animal
from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet
from project.worker import Worker


class Zoo:

    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if len(self.animals) >= self.__animal_capacity:
            return "Not enough space for animal"
        else:
            if self.__budget < price:
                return "Not enough budget"
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if len(self.workers) >= self.__workers_capacity:
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        salaries = 0
        for worker in self.workers:
            salaries += worker.salary
        if self.__budget >= salaries:
            self.__budget -= salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        costs = 0
        for animal in self.animals:
            costs += animal.money_for_care

        if self.__budget >= costs:
            self.__budget -= costs
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount


    def animals_status(self):
        x = "\n"
        result = f"You have {len(self.animals)} animals{x}"
        lions = []
        tigers = []
        cheetahs = []

        for animal in self.animals:
            if animal.__class__.__name__ == "Lion":
                lions.append(animal)
            if animal.__class__.__name__ == "Tiger":
                tigers.append(animal)
            if animal.__class__.__name__ == "Cheetah":
                cheetahs.append(animal)
        result += f"----- {len(lions)} Lions:{x}"
        for lin in lions:
            result += repr(lin) + f"{x}"

        result += f"----- {len(tigers)} Tigers:{x}"
        for tgr in tigers:
            result += repr(tgr) + f"{x}"

        result += f"----- {len(cheetahs)} Cheetahs:{x}"
        for cheet in cheetahs:
            result += repr(cheet) + f"{x}"

        return result.strip()

    def workers_status(self):
        x = "\n"
        result = f"You have {len(self.workers)} workers{x}"
        keepers = []
        caretakers = []
        vets = []
        for worker in self.workers:
            if worker.__class__.__name__ == "Keeper":
                keepers.append(worker)
            if worker.__class__.__name__ == "Caretaker":
                caretakers.append(worker)
            if worker.__class__.__name__ == "Vet":
                vets.append(worker)
        result += f"----- {len(keepers)} Keepers:{x}"
        for kpr in keepers:
            result += repr(kpr) + f"{x}"
        result += f"----- {len(caretakers)} Caretakers:{x}"
        for ctr in caretakers:
            result += repr(ctr) + f"{x}"
        result += f"----- {len(vets)} Vets:{x}"
        for vt in vets:
            result += repr(vt) + f"{x}"
        return result.strip()







