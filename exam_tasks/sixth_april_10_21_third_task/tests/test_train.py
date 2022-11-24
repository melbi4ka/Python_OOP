import unittest

from project.train.train import Train


class PetShopTest(unittest.TestCase):

    def setUp(self) -> None:
        self.train = Train("Chaika", 5)

    def test__is_initialize_proper(self):
        self.assertEqual("Chaika", self.train.name)
        self.assertEqual(5, self.train.capacity)
        self.assertEqual([], self.train.passengers)

    def test__add__if_capacity_is_full__raise(self):
        self.train.passengers = ["A", "B", "C", "D", "E"]
        with self.assertRaises(ValueError) as ex:
            self.train.add("M")
        self.assertEqual("Train is full", str(ex.exception))

    def test__add__if_passanger_exist__raise(self):
        self.train.passengers = ["A", "B", "C", "D"]
        with self.assertRaises(ValueError) as ex:
            self.train.add("A")
        self.assertEqual("Passenger A Exists", str(ex.exception))

    def test__add__if_passanger_not_exist_and_space__raise(self):
        self.train.passengers = ["A", "B", "C", "D"]
        result = self.train.add("M")
        self.assertEqual("Added passenger M", result)
        self.assertEqual(["A", "B", "C", "D", "M"], self.train.passengers)

    def test__remove__if_passanger_not_exist__raise(self):
        self.train.passengers = ["A", "B", "C", "D"]
        with self.assertRaises(ValueError) as ex:
            self.train.remove("M")
        self.assertEqual("Passenger Not Found", str(ex.exception))
        self.assertEqual(["A", "B", "C", "D"], self.train.passengers)

    def test__remove__if_passanger_not_exist__raise(self):
        self.train.passengers = ["A", "B", "C", "D"]
        with self.assertRaises(ValueError) as ex:
            self.train.remove("M")
        self.assertEqual("Passenger Not Found", str(ex.exception))
        self.assertEqual(["A", "B", "C", "D"], self.train.passengers)

    def test__remove__if_passanger_not_exist(self):
        self.train.passengers = ["A", "B", "C", "D"]
        result = self.train.remove("A")
        self.assertEqual("Removed A", result)
        self.assertEqual(["B", "C", "D"], self.train.passengers)


