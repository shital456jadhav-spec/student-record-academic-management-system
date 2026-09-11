# Student Record and Academic Management System

Unit 1 console-based prototype for Computational Thinking and Basic Programming.

## Features

- Add a student record with roll number, department, semester, subject marks, and attendance.
- Display all student records in a formatted table.
- Search by roll number or part of a student's name.
- Calculate and display the average mark and grade.
- Validate duplicate roll numbers, blank text, semester range, marks, attendance, and menu choices.

## Run the program

```bash
python student_record_system.py
```

The program uses three subjects for the prototype: Python, Mathematics, and Database.

## Run the tests

From the project directory:

```bash
python -m unittest discover -s tests -v
```

## Files

- `student_record_system.py` - menu-driven Python source code.
- `tests/test_student_record_system.py` - automated checks for calculation and search logic.
- `assignment_report.docx` - completed assignment documentation.
- `docs/flowcharts/` - flowchart images used in the report.
- `docs/sample_console_output.png` - sample console evidence.

## GitHub upload

Create a repository named `student-record-academic-management-system`, then run:

```bash
git init
git add .
git commit -m "Initial Student Record System Unit 1 submission"
git branch -M main
git remote add origin <your-github-repository-url>
git push -u origin main
```