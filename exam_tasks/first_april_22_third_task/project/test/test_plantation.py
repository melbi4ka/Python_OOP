from project.plantation import Plantation
import unittest


class PlantationTest(unittest.TestCase):

    def setUp(self) -> None:
        self.plantation = Plantation(5)

    def test_initialize_proper(self):
        self.assertEqual(5, self.plantation.size)
        self.assertEqual([], self.plantation.workers)
        self.assertEqual({}, self.plantation.plants)

    def test_initialize_size_if_negative(self):
        with self.assertRaises(ValueError) as ex:
            self.plantation.size = -5
        self.assertEqual("Size must be positive number!", str(ex.exception))

    def test_hire_worker_if_exist_raises(self):
        self.plantation.workers = ["a", "b", "c", "d"]
        with self.assertRaises(ValueError) as ex:
            self.plantation.hire_worker("b")
        self.assertEqual("Worker already hired!", str(ex.exception))

    def test_hire_worker_if_not_exist(self):
        self.plantation.workers = ["a", "b", "c", "d"]
        result = self.plantation.hire_worker("m")
        self.assertEqual(f"m successfully hired.", result)
        self.assertEqual(["a", "b", "c", "d", "m"], self.plantation.workers)

    def test_len_plants(self):
        self.plantation.plants = {"a": ["1", "2"], "b": ["1", "2", "3"]}
        result = len(self.plantation)
        self.assertEqual(5, result)

    def test_planting_if_not_worker_raises(self):
        self.plantation.workers = ["a", "b", "c", "d"]
        with self.assertRaises(ValueError)as ex:
            self.plantation.planting("m", "ab")
        self.assertEqual(f"Worker with name m is not hired!", str(ex.exception))

    def test_planting_if_plantation_is_full_raises(self):
        self.plantation.workers = ["a", "b", "c", "d", "e"]
        self.plantation.plants = {"a": ["1", "2"], "b": ["1", "2", "3", "4"]}
        with self.assertRaises(ValueError) as ex:
            self.plantation.planting("a", "ab")
        self.assertEqual("The plantation is full!", str(ex.exception))

    def test_planting_if_plantation_is_not_first(self):
        self.plantation.workers = ["a", "b", "c"]
        self.plantation.plants = {"a": ["1", "2"], "b": ["1", "2"]}
        result = self.plantation.planting("a", "6")
        self.assertEqual("a planted 6.", result)
        self.assertEqual({"a": ["1", "2", "6"], "b": ["1", "2"]}, self.plantation.plants)

    def test_planting_if_plantation_is_first(self):
        self.plantation.workers = ["a", "b", "c"]
        self.plantation.plants = {"a": ["1", "2"], "b": ["1", "2"]}
        result = self.plantation.planting("c", "6")
        self.assertEqual("c planted it's first 6.", result)
        self.assertEqual({"a": ["1", "2"], "b": ["1", "2"], "c": ["6"]}, self.plantation.plants)

    def test_str(self):
        self.plantation.workers = ["a", "b"]
        self.plantation.plants = {"a": ["1", "2"], "b": ["1", "2"]}
        my_res = "Plantation size: 5\na, b\na planted: 1, 2\nb planted: 1, 2"
        self.assertEqual(my_res, str(self.plantation))

    def test_repr(self):
        self.plantation.workers = ["a", "b"]
        self.plantation.plants = {"a": ["1", "2"], "b": ["1", "2"]}
        my_res = "Size: 5\nWorkers: a, b"
        self.assertEqual(my_res, repr(self.plantation))


if __name__== "__main__":
    unittest.main()

