try:
    from .grade_calculator import pass_status
except ImportError:  # Supports running modules directly from the src folder.
    from grade_calculator import pass_status


def rank_students(students):
    """Rank students by total marks, using roll number as a tie-breaker."""
    ranked = sorted(
        students,
        key=lambda student: (-student.total(), student.roll_no)
    )
    return [(position, student) for position, student in enumerate(ranked, start=1)]


def find_position(students, roll_no: int):
    for position, student in rank_students(students):
        if student.roll_no == roll_no:
            return position
    return None
