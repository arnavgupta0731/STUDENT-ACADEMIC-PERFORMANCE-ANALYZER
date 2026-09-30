try:
    from .grade_calculator import overall_grade, pass_status, subject_grade
except ImportError:  # Supports running modules directly from the src folder.
    from grade_calculator import overall_grade, pass_status, subject_grade


def student_report(student):
    marks = student.marks
    if not marks:
        return {
            "total": 0,
            "average": 0.0,
            "highest_subject": "N/A",
            "highest_mark": 0,
            "lowest_subject": "N/A",
            "lowest_mark": 0,
            "passed": False,
            "grade": "N/A",
        }

    highest_subject = max(marks, key=marks.get)
    lowest_subject = min(marks, key=marks.get)
    average = student.average()
    return {
        "total": student.total(),
        "average": average,
        "highest_subject": highest_subject,
        "highest_mark": marks[highest_subject],
        "lowest_subject": lowest_subject,
        "lowest_mark": marks[lowest_subject],
        "passed": pass_status(marks),
        "grade": overall_grade(average),
    }


def class_average(students) -> float:
    averages = [student.average() for student in students if student.marks]
    return sum(averages) / len(averages) if averages else 0.0


def pass_fail_count(students) -> tuple[int, int]:
    passed = sum(1 for student in students if pass_status(student.marks))
    return passed, len(students) - passed


def strongest_and_weakest_subject(student):
    if not student.marks:
        return None, None
    strongest = max(student.marks, key=student.marks.get)
    weakest = min(student.marks, key=student.marks.get)
    return strongest, weakest


def performance_category(average: float) -> str:
    if average >= 85:
        return "Excellent"
    if average >= 70:
        return "Good"
    if average >= 50:
        return "Needs Improvement"
    return "At Risk"


def subject_grade_table(student):
    return {subject: subject_grade(mark) for subject, mark in student.marks.items()}
