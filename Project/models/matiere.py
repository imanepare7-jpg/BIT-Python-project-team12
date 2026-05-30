"""
models/subject.py
-----------------
Contains the Subject class representing a course.
"""


class Subject:
    """
    Represents a subject / course in the school.
    Attributes: code, name, credits, assigned teacher.
    """

    def __init__(self, code: str, name: str, credits: int,
                 teacher_id: str = ""):
        """
        Constructor for Subject.
        :param code: unique subject code (e.g. MATH101)
        :param name: full subject name
        :param credits: number of credits (int)
        :param teacher_id: ID of the assigned teacher
        """
        self.__code       = code
        self.__name       = name
        self.__credits: int = credits     # integer type
        self.__teacher_id = teacher_id

    # ── Getters ──────────────────────────────────────────────

    def get_code(self) -> str:
        """Returns the subject code."""
        return self.__code

    def get_name(self) -> str:
        """Returns the subject name."""
        return self.__name

    def get_credits(self) -> int:
        """Returns the number of credits."""
        return self.__credits

    def get_teacher_id(self) -> str:
        """Returns the assigned teacher's ID."""
        return self.__teacher_id

    # ── Setter ───────────────────────────────────────────────

    def set_teacher(self, teacher_id: str):
        """Assigns a teacher to this subject."""
        self.__teacher_id = teacher_id

    # ── Display ──────────────────────────────────────────────

    def display_info(self):
        """Displays subject information."""
        teacher = self.__teacher_id if self.__teacher_id else "Not assigned"
        print(f"  [{self.__code}] {self.__name} — "
              f"{self.__credits} credit(s) — Teacher ID: {teacher}")

    # ── JSON Serialization ────────────────────────────────────

    def to_dict(self) -> dict:
        """Converts the subject to a dictionary for JSON saving."""
        return {
            "code":       self.__code,
            "name":       self.__name,
            "credits":    self.__credits,
            "teacher_id": self.__teacher_id
        }

    @staticmethod
    def from_dict(data: dict) -> "Subject":
        """Recreates a Subject object from a dictionary."""
        return Subject(
            data["code"],
            data["name"],
            data["credits"],
            data.get("teacher_id", "")
        )
