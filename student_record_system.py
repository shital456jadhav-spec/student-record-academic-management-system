"""
Student Record and Academic Management System
Computational Thinking and Basic Programming - Unit 1

Console-based prototype using lists, dictionaries, functions, loops,
conditional statements, and input validation.
"""

SUBJECTS = ("Python", "Mathematics", "Database")
students = []


def calculate_average(marks):
    """Return the average of a dictionary of subject marks."""
    if not marks:
        return 0.0
    return sum(marks.values()) / len(marks)


def calculate_grade(average):
    """Return a grade based on the average mark."""
    if average >= 90:
        return "A+"
    if average >= 80:
        return "A"
    if average >= 70:
        return "B"
    if average >= 60:
        return "C"
    if average >= 50:
        return "D"
    return "F"


def find_student(roll_number):
    """Find and return a student dictionary by roll number."""
    for student in students:
        if student["roll_number"].lower() == roll_number.lower():
            return student
    return None


def read_integer(prompt, minimum=None, maximum=None):
    """Read an integer and keep asking until it meets the given limits."""
    while True:
        try:
            value = int(input(prompt).strip())
            if minimum is not None and value < minimum:
                print(f"Please enter a value from {minimum} onwards.")
                continue
            if maximum is not None and value > maximum:
                print(f"Please enter a value up to {maximum}.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def read_non_empty(prompt):
    """Read text that cannot be blank."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be blank.")


def add_student():
    """Read and add one student record."""
    print("\n--- Add Student Record ---")
    roll_number = read_non_empty("Enter roll number: ")

    if find_student(roll_number) is not None:
        print("Error: a student with this roll number already exists.")
        return

    name = read_non_empty("Enter student name: ")
    department = read_non_empty("Enter department: ")
    semester = read_integer("Enter semester (1-8): ", 1, 8)

    marks = {}
    for subject in SUBJECTS:
        marks[subject] = read_integer(
            f"Enter marks for {subject} (0-100): ", 0, 100
        )

    attendance = read_integer("Enter attendance percentage (0-100): ", 0, 100)
    average = calculate_average(marks)

    student = {
        "roll_number": roll_number,
        "name": name,
        "department": department,
        "semester": semester,
        "marks": marks,
        "attendance": attendance,
        "average": average,
        "grade": calculate_grade(average),
    }
    students.append(student)
    print(f"Student record for {name} added successfully.")


def display_student(student):
    """Print one student's complete academic record."""
    print(f"\nRoll Number : {student['roll_number']}")
    print(f"Name        : {student['name']}")
    print(f"Department  : {student['department']}")
    print(f"Semester    : {student['semester']}")
    print(f"Attendance  : {student['attendance']}%")
    print("Subject Marks:")
    for subject, mark in student["marks"].items():
        print(f"  {subject:<12}: {mark}")
    print(f"Average     : {student['average']:.2f}")
    print(f"Grade       : {student['grade']}")


def display_students(records=None):
    """Display all records, or the records supplied by a search."""
    records = students if records is None else records
    print("\n--- Student Records ---")
    if not records:
        print("No student records available.")
        return

    header = (
        f"{'Roll No.':<12}{'Name':<22}{'Department':<18}"
        f"{'Sem':<6}{'Average':<10}{'Grade':<7}{'Attendance':<12}"
    )
    print(header)
    print("-" * len(header))
    for student in records:
        print(
            f"{student['roll_number']:<12}{student['name'][:20]:<22}"
            f"{student['department'][:16]:<18}{student['semester']:<6}"
            f"{student['average']:<10.2f}{student['grade']:<7}"
            f"{str(student['attendance']) + '%':<12}"
        )


def search_student():
    """Search by roll number or a part of the student's name."""
    print("\n--- Search Student ---")
    keyword = read_non_empty("Enter roll number or student name: ").lower()
    results = [
        student
        for student in students
        if keyword in student["roll_number"].lower()
        or keyword in student["name"].lower()
    ]

    if not results:
        print("No matching student found.")
        return

    for student in results:
        display_student(student)


def show_average_and_grade():
    """Display the calculated average and grade for one student."""
    print("\n--- Average and Grade ---")
    roll_number = read_non_empty("Enter roll number: ")
    student = find_student(roll_number)
    if student is None:
        print("Error: student record not found.")
        return
    print(
        f"{student['name']} has an average of "
        f"{student['average']:.2f} and grade {student['grade']}."
    )


def display_menu():
    """Display the main menu."""
    print("\n===== STUDENT RECORD AND ACADEMIC MANAGEMENT SYSTEM =====")
    print("1. Add student record")
    print("2. Display all student records")
    print("3. Search student")
    print("4. Calculate average and display grade")
    print("5. Exit")


def main():
    """Run the menu-driven application."""
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            show_average_and_grade()
        elif choice == "5":
            print("Thank you for using the Student Record System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()