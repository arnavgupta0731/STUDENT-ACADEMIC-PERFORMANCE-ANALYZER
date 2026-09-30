def subject_grade(mark: int) -> str:
    """Return a grade using the project's documented grade bands."""
    if mark >= 90:
        return "A+"
    if mark >= 80:
        return "A"
    if mark >= 70:
        return "B"
    if mark >= 60:
        return "C"
    if mark >= 50:
        return "D"
    return "F"


def overall_grade(average: float) -> str:
    return subject_grade(round(average))


def pass_status(marks: dict[str, int]) -> bool:
    return bool(marks) and all(mark >= 50 for mark in marks.values())
