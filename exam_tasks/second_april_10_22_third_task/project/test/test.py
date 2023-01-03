from project.movie import Movie

import unittest

class MovieTest(unittest.TestCase):

    def setUp(self) -> None:
        self.movie = Movie("May", 1994, 8.5)

    def test_initialize_proper_all_properties(self):
        self.assertEqual("May", self.movie.name)
        self.assertEqual(1994, self.movie.year)
        self.assertEqual(8.5, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_initialize_name_invalid_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.movie.name = ""
        self.assertEqual("Name cannot be an empty string!", str(ex.exception))

    def test_initialize_year_invalid_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.movie.year = 1400
        self.assertEqual("Year is not valid!", str(ex.exception))

    def test_add_actor_if_exist(self):
        self.movie.actors = ["Nikole", "Vigo", "Mads"]
        result = self.movie.add_actor("Vigo")
        self.assertEqual("Vigo is already added in the list of actors!", result)
        self.assertEqual(["Nikole", "Vigo", "Mads"], self.movie.actors)

    def test_add_actor_if_not_exist(self):
        self.movie.actors = ["Nikole", "Vigo", "Mads"]
        self.movie.add_actor("Joker")
        self.assertEqual(["Nikole", "Vigo", "Mads", "Joker"], self.movie.actors)

    def test_greater_than_other_film_grater(self):
        self.other_movie = Movie("June", 1995, 9)
        result = self.movie.__gt__(self.other_movie)
        self.assertEqual('"June" is better than "May"', result)

    def test_greater_than_our_film_grater(self):
        self.other_movie = Movie("June", 1995, 7)
        result = self.movie.__gt__(self.other_movie)
        self.assertEqual('"May" is better than "June"', result)

    def test_repr(self):
        self.movie.actors = ["Nikole", "Vigo", "Mads"]
        my_result = f"Name: May\nYear of Release: 1994\nRating: 8.50\nCast: Nikole, Vigo, Mads"
        self.assertEqual(my_result, repr(self.movie))


if __name__ == "__main__":
    unittest.main()
