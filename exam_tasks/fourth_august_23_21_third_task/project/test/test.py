from project.library import Library

import unittest

class LibraryTest(unittest.TestCase):

    def setUp(self) -> None:
        self.lib = Library("Alexandria")

    def test__initialize__valid_properties(self):
        self.assertEqual("Alexandria",  self.lib.name)
        self.assertEqual({}, self.lib.books_by_authors)
        self.assertEqual({}, self.lib.readers)

    def test_name__invalid_raise(self):
        with self.assertRaises(ValueError) as ex:
            self.lib.name = ""
        self.assertEqual("Name cannot be empty string!",  str(ex.exception))

    def test_add_book__if_not_author_and_book_not_exist__add(self):
        self.lib.books_by_authors = {"Twain": ["Tom"], "Stendal": ["Red"]}
        self.lib.add_book("Markes", "100")
        self.assertEqual({"Twain": ["Tom"], "Stendal": ["Red"], "Markes": ["100"]}, self.lib.books_by_authors)

    def test_add_book__if_author_and_book_not_exist__add(self):
        self.lib.books_by_authors = {"Twain": ["Tom"], "Stendal": ["Red"]}
        self.lib.add_book("Twain", "Fin")
        self.assertEqual({"Twain": ["Tom", "Fin"], "Stendal": ["Red"]}, self.lib.books_by_authors)

    def test_add_book__if_author_and_book_exist__not_add(self):
        self.lib.books_by_authors = {"Twain": ["Tom"], "Stendal": ["Red"]}
        self.lib.add_book("Twain", "Tom")
        self.assertEqual({"Twain": ["Tom"], "Stendal": ["Red"]}, self.lib.books_by_authors)

    def test_add_reader__if_reader_not_exist__add(self):
        self.lib.readers = {"Ani": [], "Gogo": [], "Peter": []}
        self.lib.add_reader("Tom")
        self.assertEqual({"Ani": [], "Gogo": [], "Peter": [], "Tom": []}, self.lib.readers)

    def test_add_reader__if_reader_exist__not_add(self):
        self.lib.readers = {"Ani": [], "Gogo": [], "Peter": []}
        result = self.lib.add_reader("Ani")
        self.assertEqual({"Ani": [], "Gogo": [], "Peter": []}, self.lib.readers)
        self.assertEqual("Ani is already registered in the Alexandria library.", result)

    def test_rent_book_if_reader_not_exist__not_rent(self):
        self.lib.readers = {"Ani": [], "Gogo": [], "Peter": []}
        result = self.lib.rent_book("Tom", "Zola", "Nana")
        self.assertEqual({"Ani": [], "Gogo": [], "Peter": []}, self.lib.readers)
        self.assertEqual("Tom is not registered in the Alexandria Library.", result)

    def test_rent_book_if_author_not_exist__not_rent(self):
        self.lib.books_by_authors = {"Twain": ["Tom"], "Stendal": ["Red"]}
        self.lib.readers = {"Ani": [], "Gogo": [], "Peter": []}
        result = self.lib.rent_book("Ani", "Zola", "Nana")
        self.assertEqual({"Twain": ["Tom"], "Stendal": ["Red"]}, self.lib.books_by_authors)
        self.assertEqual("Alexandria Library does not have any Zola's books.", result)

    def test_rent_book_if_author_exist_book_not_exist__not_rent(self):
        self.lib.books_by_authors = {"Twain": ["Tom"], "Stendal": ["Red"]}
        self.lib.readers = {"Ani": [], "Gogo": [], "Peter": []}
        result = self.lib.rent_book("Ani", "Twain", "Fin")
        self.assertEqual({"Twain": ["Tom"], "Stendal": ["Red"]}, self.lib.books_by_authors)
        self.assertEqual('''Alexandria Library does not have Twain's "Fin".''', result)

    def test_rent_book_if_all_exist__rent(self):
        self.lib.books_by_authors = {"Twain": ["Tom", "Fin"], "Stendal": ["Red"]}
        self.lib.readers = {"Ani": [], "Gogo": [], "Peter": []}
        self.lib.rent_book("Ani", "Twain", "Tom")
        self.assertEqual({"Ani": [{"Twain": "Tom"}], "Gogo": [], "Peter": []}, self.lib.readers)
        self.assertEqual({"Twain": ["Fin"], "Stendal": ["Red"]}, self.lib.books_by_authors)





