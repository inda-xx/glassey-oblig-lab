# student.py

class Student:
    def __init__(self, name):
        self.name = name
        self.completed_courses = []

    def add_completed_course(self, course):
        self.completed_courses.append(course)

    def get_completed_credits(self):
        credits = [course.credits for course in self.completed_courses]
        return sum(credits)

    def __str__(self):
        return f"{self.name} Andel avklarade: {self.get_completed_percentage(147.5):.1f}%"

    def get_completed_percentage(self, total_credits):
        return (self.get_completed_credits() / total_credits) * 100
