# main.py
import csv
from course import Course
from mediastudent import MediaStudent

# Function to read courses from the CSV file
def read_courses(filename):
    courses = []
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            code, name, credits = row
            course = Course(code, name, credits)
            courses.append(course)
    return courses

# Function to read student data from the CSV file
def read_students(filename, courses):
    students = []
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            name, *completed_courses = row
            student = MediaStudent(name)
            for code in completed_courses:
                for course in courses:
                    if course.code == code:
                        student.add_completed_course(course)
            students.append(student)
    return students

if __name__ == "__main__":
    courses = read_courses("ObligatoriskaMediakurser.csv")
    students = read_students("Studieresultat.csv", courses)
    
    total_mandatory_credits = sum(course.credits for course in courses)
    
    print("Alla obligatoriska kurser:")
    for course in courses:
        print(course)
    
    print(f"Total obligatorisk poängsumma: {total_mandatory_credits:.1f} ECTS")
    
    print("Alla studenter:")
    for student in students:
        print(student)
