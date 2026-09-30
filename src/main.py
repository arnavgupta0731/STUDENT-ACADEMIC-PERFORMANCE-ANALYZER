try:
    from .models import Student
    from .student_manager import add_student, add_or_update_mark, find_student, remove_student
    from .performance_analyzer import (
        class_average,
        pass_fail_count,
        performance_category,
        student_report,
        strongest_and_weakest_subject,
    )
    from .subject_statistics import subject_statistics
    from .ranking import find_position, rank_students
    from .reporting import print_student_report, print_class_summary, print_bar
except ImportError:  # Supports running this file directly with `python src/main.py`.
    from models import Student
    from student_manager import add_student, add_or_update_mark, find_student, remove_student
    from performance_analyzer import (
        class_average,
        pass_fail_count,
        performance_category,
        student_report,
        strongest_and_weakest_subject,
    )
    from subject_statistics import subject_statistics
    from ranking import find_position, rank_students
    from reporting import print_student_report, print_class_summary, print_bar


def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")


def add_student_flow(students):
    try:
        roll = input_int("Enter roll number: ")
        name = input("Enter student name: ")
        student = add_student(students, roll, name)

        count = input_int("How many subjects? ")
        if count <= 0:
            raise ValueError("Number of subjects must be positive.")

        for i in range(count):
            subject = input(f"Subject {i + 1}: ")
            mark = input_int("Marks (0-100): ")
            add_or_update_mark(student, subject, mark)

        print("Student record added successfully.")
    except ValueError as exc:
        print(f"Input error: {exc}")


def view_student_flow(students):
    roll = input_int("Enter roll number: ")
    student = find_student(students, roll)
    if student is None:
        print("Student not found.")
        return
    report = student_report(student)
    position = find_position(students, roll)
    print_student_report(student, report, position)


def class_summary_flow(students):
    if not students:
        print("No student records available.")
        return
    stats = subject_statistics(students)
    passed, failed = pass_fail_count(students)
    print_class_summary(students, stats, class_average(students), passed, failed)


def ranking_flow(students):
    if not students:
        print("No student records available.")
        return
    print("\nCLASS RANKING")
    print("-" * 40)
    for position, student in rank_students(students):
        print(f"{position:>2}. {student.name:<22} {student.total():>4}")


def insight_flow(students):
    roll = input_int("Enter roll number: ")
    student = find_student(students, roll)
    if student is None:
        print("Student not found.")
        return
    report = student_report(student)
    strongest, weakest = strongest_and_weakest_subject(student)
    print("\nPERFORMANCE INSIGHT")
    print("-" * 40)
    print(f"Student category : {performance_category(report['average'])}")
    print(f"Strongest subject: {strongest} ({student.marks[strongest]})")
    print(f"Weakest subject  : {weakest} ({student.marks[weakest]})")
    print("\nSubject marks")
    for subject, mark in student.marks.items():
        print_bar(subject, mark)


def delete_student_flow(students):
    roll = input_int("Enter roll number to remove: ")
    if remove_student(students, roll):
        print("Student removed.")
    else:
        print("Student not found.")


def load_demo_data(students):
    demo = [
        (101, "Aarav", {"Mathematics": 88, "Python": 94, "Physics": 76, "English": 82}),
        (102, "Meera", {"Mathematics": 92, "Python": 89, "Physics": 84, "English": 90}),
        (103, "Kabir", {"Mathematics": 74, "Python": 81, "Physics": 69, "English": 77}),
        (104, "Diya", {"Mathematics": 65, "Python": 72, "Physics": 61, "English": 70}),
    ]
    for roll, name, marks in demo:
        student = add_student(students, roll, name)
        for subject, mark in marks.items():
            add_or_update_mark(student, subject, mark)


def main():
    students = []
    print("=" * 52)
    print(" STUDENT ACADEMIC PERFORMANCE ANALYZER")
    print("=" * 52)
    print("Tip: choose option 8 to load sample records for a quick demo.")

    while True:
        print(
            "\n1. Add student\n"
            "2. View student report\n"
            "3. Class summary\n"
            "4. Class ranking\n"
            "5. Student performance insight\n"
            "6. Remove student\n"
            "7. List students\n"
            "8. Load sample data\n"
            "9. Exit"
        )
        choice = input_int("Enter choice: ")

        if choice == 1:
            add_student_flow(students)
        elif choice == 2:
            view_student_flow(students)
        elif choice == 3:
            class_summary_flow(students)
        elif choice == 4:
            ranking_flow(students)
        elif choice == 5:
            insight_flow(students)
        elif choice == 6:
            delete_student_flow(students)
        elif choice == 7:
            if students:
                for student in students:
                    print(f"{student.roll_no} - {student.name}")
            else:
                print("No student records available.")
        elif choice == 8:
            if students:
                print("Sample data can only be loaded into an empty list.")
            else:
                load_demo_data(students)
                print("Sample data loaded.")
        elif choice == 9:
            print("Thank you for using the analyzer.")
            break
        else:
            print("Please choose a number from 1 to 9.")


if __name__ == "__main__":
    main()
