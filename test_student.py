# test_student.py
import unittest
from course import Course
from student import Student

class TestStudent(unittest.TestCase):
    def test_student_creation(self):
        student = Student("Katarina")
        self.assertEqual(student.name, "Katarina")

    def test_add_completed_course(self):
        student = Student("Katarina")
        course = Course("DM1581", "Introduktion till medieteknik", 6.0)
        student.add_completed_course(course)
        self.assertIn(course, student.completed_courses)

    def test_get_completed_credits(self):
        student = Student("Katarina")
        course1 = Course("DM1581", "Introduktion till medieteknik", 6.0)
        course2 = Course("SF1625", "Envariabelanalys", 7.5)
        student.add_completed_course(course1)
        student.add_completed_course(course2)
        self.assertEqual(student.get_completed_credits(), 13.5)

if __name__ == '__main__':
    unittest.main()
