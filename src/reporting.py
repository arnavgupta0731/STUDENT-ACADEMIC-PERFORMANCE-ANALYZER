def print_student_report(student, report, position=None):
    print("\n" + "=" * 52)
    print("STUDENT PERFORMANCE REPORT")
    print("=" * 52)
    print(f"Roll No.: {student.roll_no}")
    print(f"Name    : {student.name}")
    print("-" * 52)
    for subject, mark in student.marks.items():
        print(f"{subject:<28} {mark:>3}")
    print("-" * 52)
    print(f"Total           : {report['total']}")
    print(f"Average         : {report['average']:.2f}")
    print(f"Highest         : {report['highest_subject']} ({report['highest_mark']})")
    print(f"Lowest          : {report['lowest_subject']} ({report['lowest_mark']})")
    print(f"Overall Grade   : {report['grade']}")
    print(f"Result          : {'PASS' if report['passed'] else 'FAIL'}")
    if position is not None:
        print(f"Class Position  : {position}")
    print("=" * 52)


def print_class_summary(students, subject_stats, class_avg, passed, failed):
    print("\n" + "=" * 52)
    print("CLASS PERFORMANCE SUMMARY")
    print("=" * 52)
    print(f"Students        : {len(students)}")
    print(f"Class Average   : {class_avg:.2f}")
    print(f"Passed          : {passed}")
    print(f"Failed          : {failed}")
    print("-" * 52)
    for subject, stats in sorted(subject_stats.items()):
        print(
            f"{subject:<20} Avg: {stats['average']:.2f}  "
            f"High: {stats['highest']:>3}  Low: {stats['lowest']:>3}"
        )
    print("=" * 52)


def print_bar(label, value, scale=2):
    bars = "#" * max(1, int(value / scale))
    print(f"{label:<20} {bars} {value:.1f}")
