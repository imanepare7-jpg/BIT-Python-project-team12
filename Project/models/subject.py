class Subject:
    def __init__(self, code, name, credits,
                 teacher_id= ""):
        """
        Constructor for Subject.
        """
        self.code = code
        self.name = name
        self.credits = credits     # integer type
        self.teacher_id = teacher_id

    def get_code(self) -> str:
        """Returns the subject code."""
        return self.code

    def get_name(self) -> str:
        """Returns the subject name."""
        return self.name

    def get_credits(self) -> int:
        """Returns the number of credits."""
        return self.credits

    def get_teacher_id(self) -> str:
        """Returns the assigned teacher's ID."""
        return self.teacher_id

    def set_teacher(self, teacher_id: str):
        """Assigns a teacher to this subject."""
        self.teacher_id = teacher_id

    def display_info(self):
        """Displays subject information."""
        teacher = self.teacher_id if self.teacher_id else "Not assigned"
        print(f"  [{self.code}] {self.name} — "
              f"{self.credits} credit(s) — Teacher ID: {teacher}")

    def to_dict(self) -> dict:
        """Converts the subject to a dictionary for JSON saving."""
        return {
            "code": self.code,
            "name": self.name,
            "credits": self.credits,
            "teacher_id": self.teacher_id
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
