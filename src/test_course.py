# test_course.py
import unittest
from course import Course

class TestCourse(unittest.TestCase):
    def test_course_creation(self):
        course = Course("DM1581", "Introduktion till medieteknik", 6.0)
        self.assertEqual(course.code, "DM1581")
        self.assertEqual(course.name, "Introduktion till medieteknik")
        self.assertEqual(course.credits, 6.0)

if __name__ == '__main__':
    unittest.main()
