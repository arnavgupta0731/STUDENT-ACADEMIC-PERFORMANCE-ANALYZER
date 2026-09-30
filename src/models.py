class Student:
    def __init__(self, roll_no: int, name: str):
        self.roll_no = roll_no
        self.name = name
        self.marks = {}

    def total(self) -> int:
        return sum(self.marks.values())

    def average(self) -> float:
        return self.total() / len(self.marks) if self.marks else 0.0
