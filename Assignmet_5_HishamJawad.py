import json

# Course class to represent each course
class Course:
    def __init__(self, code, name, credit_hours, is_core):
        self.code = code
        self.name = name
        self.credit_hours = credit_hours
        self.is_core = is_core

    def __str__(self):
        return f"Course Code: {self.code}, Name: {self.name}, Credit Hours: {self.credit_hours}, Core: {self.is_core}"

# Student class to represent each student and their enrolled courses
class Student:
    def __init__(self, student_id, name):
        self.id = student_id
        self.name = name
        self.enrolled_courses = {}  # Dictionary to store enrolled courses

    def enroll(self, course):
        if course.code in self.enrolled_courses:
            print("Student is already enrolled in this course.")
        else:
            self.enrolled_courses[course.code] = course

    def drop(self, course_code):
        if course_code not in self.enrolled_courses:
            print("Course not found in student's enrollment list.")
        else:
            del self.enrolled_courses[course_code]

    def list_courses(self):
        if not self.enrolled_courses:
            print("No courses enrolled.")
        else:
            for course in self.enrolled_courses.values():
                print(course)

# Function to add a new course to the catalog
def add_course(courses):
    code = input("Enter course code: ")
    name = input("Enter course name: ")
    credit_hours = int(input("Enter credit hours: "))
    is_core = input("Is it a core course? (y/n): ").lower() == 'y'
    course = Course(code, name, credit_hours, is_core)
    courses[code] = course
    print("Course added successfully!")

# Function to enroll a student in a course
def enroll_student(students, courses):
    student_id = input("Enter student ID: ")
    course_code = input("Enter course code: ")
    
    student = None
    for s in students:  # Using a basic loop to find the student
        if s.id == student_id:
            student = s
            break

    course = courses.get(course_code)

    if not student:
        print("Student not found.")
        return
    if not course:
        print("Course not found.")
        return

    student.enroll(course)

# Function to drop a course for a student
def drop_course(students):
    student_id = input("Enter student ID: ")
    course_code = input("Enter course code: ")
    
    student = None
    for s in students:  # Using a loop to find the student
        if s.id == student_id:
            student = s
            break

    if not student:
        print("Student not found.")
        return

    student.drop(course_code)

# Function to list all courses a student is enrolled in
def list_student_courses(students):
    student_id = input("Enter student ID: ")
    
    student = None
    for s in students:  # Looping through to find the student
        if s.id == student_id:
            student = s
            break

    if not student:
        print("Student not found.")
        return

    print(f"Courses for {student.name}:")
    student.list_courses()

# Function to save the course catalog to a file
def save_course_catalog(courses):
    with open('course_catalog.json', 'w') as file:
        courses_dict = {code: course.__dict__ for code, course in courses.items()}
        json.dump(courses_dict, file)
    print("Course catalog saved successfully!")

# Function to load the course catalog from a file
def load_course_catalog(courses):
    with open('course_catalog.json', 'r') as file:
        courses_dict = json.load(file)
        for code, course_data in courses_dict.items():
            courses[code] = Course(**course_data)
    print("Course catalog loaded successfully!")

# Main function to drive the menu-driven interface
def main():
    students = []
    courses = {}

    while True:
        print("\n1. Add Course")
        print("2. Enroll Student in Course")
        print("3. Drop Course for Student")
        print("4. List Student Courses")
        print("5. Save Course Catalog")
        print("6. Load Course Catalog")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_course(courses)
        elif choice == '2':
            enroll_student(students, courses)
        elif choice == '3':
            drop_course(students)
        elif choice == '4':
            list_student_courses(students)
        elif choice == '5':
            save_course_catalog(courses)
        elif choice == '6':
            load_course_catalog(courses)
        elif choice == '7':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

