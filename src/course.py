# course.py

class Course:
    def __init__(self, code, name, credits):
        self.code = code
        self.name = name
        self.credits = float(credits)

    def __str__(self):
        return f"{self.code} {self.name} {self.credits} ECTS"
