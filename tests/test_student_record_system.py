import unittest

import student_record_system as system


class StudentRecordSystemTests(unittest.TestCase):
    def setUp(self):
        system.students.clear()

    def test_average_calculation(self):
        marks = {"Python": 80, "Mathematics": 70, "Database": 90}
        self.assertAlmostEqual(system.calculate_average(marks), 80.0)

    def test_grade_boundaries(self):
        self.assertEqual(system.calculate_grade(90), "A+")
        self.assertEqual(system.calculate_grade(80), "A")
        self.assertEqual(system.calculate_grade(70), "B")
        self.assertEqual(system.calculate_grade(60), "C")
        self.assertEqual(system.calculate_grade(50), "D")
        self.assertEqual(system.calculate_grade(49.99), "F")

    def test_find_student_is_case_insensitive(self):
        system.students.append(
            {
                "roll_number": "ST101",
                "name": "Asha Rao",
                "department": "Computer Science",
                "semester": 2,
                "marks": {"Python": 80, "Mathematics": 80, "Database": 80},
                "attendance": 90,
                "average": 80,
                "grade": "A",
            }
        )
        self.assertEqual(system.find_student("st101")["name"], "Asha Rao")

    def test_zero_marks_produce_fail_grade(self):
        marks = {"Python": 0, "Mathematics": 0, "Database": 0}
        self.assertEqual(system.calculate_average(marks), 0)
        self.assertEqual(system.calculate_grade(0), "F")


if __name__ == "__main__":
    unittest.main()