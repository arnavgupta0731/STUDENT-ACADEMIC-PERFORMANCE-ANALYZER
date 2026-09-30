def subject_statistics(students):
    subjects = {}
    for student in students:
        for subject, mark in student.marks.items():
            subjects.setdefault(subject, []).append(mark)

    result = {}
    for subject, marks in subjects.items():
        result[subject] = {
            "average": sum(marks) / len(marks),
            "highest": max(marks),
            "lowest": min(marks),
            "passed": sum(1 for mark in marks if mark >= 50),
            "failed": sum(1 for mark in marks if mark < 50),
        }
    return result


def subject_average_ranking(students):
    stats = subject_statistics(students)
    return sorted(stats.items(), key=lambda item: item[1]["average"], reverse=True)
