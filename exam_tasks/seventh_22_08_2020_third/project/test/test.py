import unittest

from project.student_report_card import StudentReportCard


class StudentReportCardTest(unittest.TestCase):

    def setUp(self) -> None:
        self.student_card = StudentReportCard("Mel", 11)

    def test__init__if_initialize_proper(self):
        self.assertEqual("Mel", self.student_card.student_name)
        self.assertEqual(11, self.student_card.school_year)
        self.assertEqual({}, self.student_card.grades_by_subject)

    def test__init__if_grades_by_subject_is_not_empty(self):
        self.student_card.grades_by_subject = {"Maths": [5, 5, 6]}
        self.assertEqual({"Maths": [5, 5, 6]}, self.student_card.grades_by_subject)

    def test__name__if__name_is_empty__raise(self):
        with self.assertRaises(ValueError) as ex:
            self.student_card.student_name = ""
        self.assertEqual("Student Name cannot be an empty string!", str(ex.exception))

    def test__school_year_if_year_not_between_one_and_twelve_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.student_card.school_year = 20
        self.assertEqual("School Year must be between 1 and 12!", str(ex.exception))
        with self.assertRaises(ValueError) as ex:
            self.student_card.school_year = 0
        self.assertEqual("School Year must be between 1 and 12!", str(ex.exception))
        with self.assertRaises(ValueError) as ex:
            self.student_card.school_year = -5
        self.assertEqual("School Year must be between 1 and 12!", str(ex.exception))

    # def test__school_year_if_year_is_between_one_and_twelve_raises(self):
    #     for grade in range(1, 13):
    #         self.student_card.school_year = grade
    #         self.assertEqual(grade, self.student_card.school_year)
    def test_school_year_between_one_twelve(self):
        self.student_card.school_year = 1
        self.assertEqual(1, self.student_card.school_year)
        self.student_card.school_year = 12
        self.assertEqual(12, self.student_card.school_year)


    def test_add_grade_if_subject_not_exist(self):
        self.student_card.grades_by_subject = {}
        self.student_card.add_grade("Maths", 5)
        self.assertEqual({"Maths": [5]}, self.student_card.grades_by_subject)

    def test_add_grade_if_subject_exist(self):
        self.student_card.grades_by_subject = {"Maths": [5]}
        self.student_card.add_grade("Maths", 6)
        self.assertEqual({"Maths": [5, 6]}, self.student_card.grades_by_subject)

    def test_average_grade_by_the_subject(self):
        self.student_card.grades_by_subject = {"Maths": [5.5, 5.20, 5.50], "Development": [4.5, 6.0, 6.0]}
        result = self.student_card.average_grade_by_subject()
        self.assertEqual(f"Maths: 5.40\nDevelopment: 5.50", result)

        self.student_card.grades_by_subject = {"Maths": [5.0, 5.0, 5.0]}
        result = self.student_card.average_grade_by_subject()
        self.assertEqual(f"Maths: 5.00", result)

    def test_average_grade_for_all_subject(self):
        self.student_card.grades_by_subject = {"Maths": [5.5, 5.2, 5.5], "Development": [4.5, 6, 6]}
        result = self.student_card.average_grade_for_all_subjects()
        self.assertEqual("Average Grade: 5.45", result)

    def test__repr(self):
        self.student_card.grades_by_subject = {"Maths": [5, 5, 5], "Development": [4, 6, 6]}
        report = f"Name: Mel\nYear: 11\n----------\nMaths: 5.00\nDevelopment: 5.33\n----------\nAverage Grade: 5.17"
        self.assertEqual(report, repr(self.student_card))


if __name__ == "__main__":
    unittest.main()
