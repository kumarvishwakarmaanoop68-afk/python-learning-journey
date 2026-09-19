# Student Management System
# Day 8 mini project

import json

FILE_NAME = "students.json"


def load_students():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


def add_student(students):
    name = input("Enter student name: ").strip()
    course = input("Enter course: ").strip()

    student = {
        "name": name,
        "course": course
    }

    students.append(student)
    save_students(students)
    print("Student added successfully.")


def view_students(students):
    if not students:
        print("No students found.")
        return

    for index, student in enumerate(students, start=1):
        print(f"{index}. {student['name']} - {student['course']}")


def search_student(students):
    name = input("Enter name to search: ").strip().lower()

    found = False

    for student in students:
        if student["name"].lower() == name:
            print("Found:", student["name"], "-", student["course"])
            found = True

    if not found:
        print("Student not found.")


def main():
    students = load_students()

    while True:
        print("\n--- Student Management System ---")
        print("1. Add student")
        print("2. View students")
        print("3. Search student")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
