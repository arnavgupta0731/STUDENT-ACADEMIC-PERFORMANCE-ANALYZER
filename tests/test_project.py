import sys
from pathlib import Path

# Make the project root importable when this file is run directly.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.models import Student
from src.grade_calculator import subject_grade, overall_grade, pass_status
from src.performance_analyzer import student_report, performance_category
from src.ranking import rank_students
from src.subject_statistics import subject_statistics


def test_grades():
    assert subject_grade(95) == "A+"
    assert subject_grade(84) == "A"
    assert subject_grade(72) == "B"
    assert subject_grade(61) == "C"
    assert subject_grade(50) == "D"
    assert subject_grade(49) == "F"


def test_student_report():
    student = Student(1, "Test")
    student.marks = {"Math": 90, "Python": 80}

    report = student_report(student)

    assert report["total"] == 170
    assert report["average"] == 85
    assert report["highest_mark"] == 90
    assert report["lowest_mark"] == 80
    assert report["passed"] is True
    assert overall_grade(report["average"]) == "A"


def test_fail_status():
    assert pass_status({"Math": 80, "Python": 49}) is False


def test_ranking():
    first = Student(1, "A")
    first.marks = {"Math": 90}

    second = Student(2, "B")
    second.marks = {"Math": 80}

    ranked = rank_students([second, first])

    assert ranked[0][0] == 1
    assert ranked[0][1].name == "A"


def test_subject_statistics():
    students = [
        Student(1, "A"),
        Student(2, "B"),
    ]
    students[0].marks = {"Math": 80, "Python": 90}
    students[1].marks = {"Math": 60, "Python": 70}

    stats = subject_statistics(students)

    assert stats["Math"]["average"] == 70
    assert stats["Math"]["highest"] == 80
    assert stats["Math"]["lowest"] == 60
    assert stats["Math"]["passed"] == 2
    assert stats["Math"]["failed"] == 0


def test_performance_category():
    assert performance_category(90) == "Excellent"
    assert performance_category(75) == "Good"
    assert performance_category(55) == "Needs Improvement"
    assert performance_category(40) == "At Risk"


if __name__ == "__main__":
    tests = [
        test_grades,
        test_student_report,
        test_fail_status,
        test_ranking,
        test_subject_statistics,
        test_performance_category,
    ]

    for test in tests:
        test()

    print("All tests passed.")
