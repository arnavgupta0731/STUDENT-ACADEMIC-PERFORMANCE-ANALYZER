def validate_name(name: str) -> str:
    name = name.strip()
    if not name:
        raise ValueError("Name cannot be empty.")
    if any(ch.isdigit() for ch in name):
        raise ValueError("Name should not contain numbers.")
    return name


def validate_roll_no(roll_no: int) -> int:
    if roll_no <= 0:
        raise ValueError("Roll number must be positive.")
    return roll_no


def validate_mark(mark: int) -> int:
    if mark < 0 or mark > 100:
        raise ValueError("Marks must be between 0 and 100.")
    return mark


def validate_subject(subject: str) -> str:
    subject = subject.strip()
    if not subject:
        raise ValueError("Subject name cannot be empty.")
    return subject
