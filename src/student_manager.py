try:
    from .models import Student
    from .validation import validate_mark, validate_name, validate_roll_no, validate_subject
except ImportError:  # Supports running modules directly from the src folder.
    from models import Student
    from validation import validate_mark, validate_name, validate_roll_no, validate_subject


def add_student(students: list[Student], roll_no: int, name: str) -> Student:
    validate_roll_no(roll_no)
    validate_name(name)
    if any(student.roll_no == roll_no for student in students):
        raise ValueError("A student with this roll number already exists.")
    student = Student(roll_no, name)
    students.append(student)
    return student


def add_or_update_mark(student: Student, subject: str, mark: int) -> None:
    subject = validate_subject(subject)
    validate_mark(mark)
    student.marks[subject] = mark


def find_student(students: list[Student], roll_no: int) -> Student | None:
    for student in students:
        if student.roll_no == roll_no:
            return student
    return None


def remove_student(students: list[Student], roll_no: int) -> bool:
    student = find_student(students, roll_no)
    if student is None:
        return False
    students.remove(student)
    return True


def subject_names(students: list[Student]) -> list[str]:
    names = set()
    for student in students:
        names.update(student.marks.keys())
    return sorted(names)
