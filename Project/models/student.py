from models.person import Person
from constants     import PASSING_GRADE, MENTIONS, MENTION_THRESHOLDS

class Student(Person):
    """
    Represents a student. Inherits from Person.
    Adds: class level, date of birth, grades, absences.
    Demonstrates: inheritance, encapsulation, polymorphism.
    """

    def __init__(self, id, last_name, first_name, email, class_level, date_of_birth):
        super().init__(id, last_name, first_name, email)  # call parent constructor
        self.class_level = class_level
        self.date_of_birth = date_of_birth
        self.grades: dict  = {}    # {subject: [grade1, grade2, ...]}
        self.absences: list = []   # [{"date": ..., "subject": ...}]

    def get_class_level(self) -> str:
        """Returns the student's class level."""
        return self.class_level

    def get_grades(self) -> dict:
        """Returns the grades dictionary."""
        return self.grades

    def get_absences(self) -> list:
        """Returns the list of absences."""
        return self.absences

    def get_absence_count(self) -> int:
        """Returns the total number of absences."""
        return len(self.absences)

    def add_grade(self, subject, grade):
        """
        Adds a grade for a given subject.
        """
        if subject not in self.grades:
            self.grades[subject] = []
        self.grades[subject].append(grade)

    def get_subject_average(self, subject) -> float:
        """
        Calculates the average for a subject.
        """
        if subject in self.grades and len(self.grades[subject]) > 0:
            return sum(self.grades[subject]) / len(self.grades[subject])
        return 0.0

    def get_overall_average(self) -> float:
        """Calculates the overall average across all subjects."""
        if not self.grades:
            return 0.0
        averages = [self.get_subject_average(s) for s in self.grades]
        return sum(averages) / len(averages)

    def is_passing(self) -> bool:
        """Returns True if the overall average is >= the passing grade."""
        return self.get_overall_average() >= PASSING_GRADE

    def get_mention(self) -> str:
        """
        Returns the grade mention based on the overall average.
        Uses the MENTIONS and MENTION_THRESHOLDS tuples from constants.py
        """
        average: float = self.get_overall_average()
        current_mention: str = MENTIONS[0]   # "Fail" by default
        for i in range(len(MENTION_THRESHOLDS)):
            if average >= MENTION_THRESHOLDS[i]:
                current_mention = MENTIONS[i]
        return current_mention

    def add_absence(self, date: str, subject: str):
        """
        Records an absence.
        """
        self.absences.append({"date": date, "subject": subject})

    def display_info(self):
        """
        Displays full student information.
        Overrides the Person method — polymorphism.
        """
        print(f"\n{'='*45}")
        print(f"  STUDENT  : {self.get_full_name()}")
        print(f"{'='*45}")
        super().display_info()       # call parent method
        print(f"  Class : {self.class_level}")
        print(f"  DOB : {self.date_of_birth}")
        print(f"  Absences : {self.get_absence_count()}")
        avg = self.get_overall_average()
        status = "PASSING ✓" if self.is_passing() else "FAILING ✗"
        print(f"  Average  : {avg:.2f}/20  ({status})")
        print(f"  Mention  : {self.get_mention()}")

    def to_dict(self) -> dict:
        """Converts the student to a dictionary for JSON saving."""
        data = super().to_dict()
        data["type"] = "student"
        data["class_level"]  = self.class_level
        data["date_of_birth"] = self.date_of_birth
        data["grades"] = self.grades
        data["absences"] = self.absences
        return data

    @staticmethod
    def from_dict(data: dict) -> "Student":
        """Recreates a Student object from a dictionary (file loading)."""
        s = Student(
            data["id"], data["last_name"], data["first_name"], data["email"],
            data["class_level"], data["date_of_birth"]
        )
        s._Student__grades   = data.get("grades", {})
        s._Student__absences = data.get("absences", [])
        return s
