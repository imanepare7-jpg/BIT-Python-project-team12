"""
models/teacher.py
-----------------
This module defines the teacher class, which extends the person class.
It stores teacher-specific information such as specialisation,
phone number, and subjects taught .
"""

from models.person import Person


class Teacher(Person):
    """
    CLASS DESCRIPTION
    Represents a teacher in the school management system
    """
    def __init__(self, id: str, last_name: str, first_name: str, email: str,
                 specialization: str, phone: str):
        """
        :Constructor for Teacher.
        :param specialization: area of expertise
        :param phone: phone number
        """
        super().__init__(id, last_name, first_name, email)  # parent constructor
        self.__specialization = specialization
        self.__phone          = phone
        self.__subjects: list = []
    # ── Getters ──────────────────────────────────────────────

    def get_specialization(self) -> str:
        """Returns the teacher's specialization."""
        return self.__specialization
        
    def get_phone(self) -> str:
        """Returns the phone number."""
        return self.__phone
        
    def get_subjects(self) -> list:
        """Returns the list of subjects taught."""
        return self.__subjects
        
    # ── Methods ──────────────────────────────────────────────

    def add_subject(self, subject: str):
        """Adds a subject to the list if not already present."""
        if subject not in self.__subjects:
            self.__subjects.append(subject)


    # ── JSON Serialization ────────────────────────────────────

    def to_dict(self) -> dict:
        """Converts the teacher to a dictionary for JSON saving."""
        data = super().to_dict()
        data["type"]           = "teacher"
        data["specialization"] = self.__specialization
        data["phone"]          = self.__phone
        data["subjects"]       = self.__subjects
        return data
        
    @staticmethod
    def from_dict(data: dict) -> "Teacher":
        """Recreates a Teacher object from a dictionary."""
        t = Teacher(
            data["id"], data["last_name"], data["first_name"], data["email"],
            data["specialization"], data["phone"]
        )
        t._Teacher__subjects = data.get("subjects", [])
        return t
 #── Display (polymorphism) ────────────────────────────────

    def display_info(self):
        """
        Displays full teacher information.
        Overrides the Person method — polymorphism.
        """
        print(f"\n{'='*45}")
        print(f"  TEACHER      : {self.get_full_name()}")
        print(f"{'='*45}")
        super().display_info()       # call parent method
        print(f"  Specialization : {self.__specialization}")
        print(f"  Phone          : {self.__phone}")
        subjects_str = ", ".join(self.__subjects) if self.__subjects else "None"
        print(f"  Subjects       : {subjects_str}")

    # ── JSON Serialization ────────────────────────────────────

    def to_dict(self) -> dict:
        """Converts the teacher to a dictionary for JSON saving."""
        data = super().to_dict()
        data["type"]           = "teacher"
        data["specialization"] = self.__specialization
        data["phone"]          = self.__phone
        data["subjects"]       = self.__subjects
        return data

    @staticmethod
    def from_dict(data: dict) -> "Teacher":
        """Recreates a Teacher object from a dictionary."""
        t = Teacher(
            data["id"], data["last_name"], data["first_name"], data["email"],
            data["specialization"], data["phone"]
        )
        t._Teacher__subjects = data.get("subjects", [])
        return t
        

    # ── Display (polymorphism) ────────────────────────────────

    def display_info(self):
        """
        Displays full teacher information.
        Overrides the Person method — polymorphism.
        """
        print(f"\n{'='*45}")
        print(f"  TEACHER      : {self.get_full_name()}")
        print(f"{'='*45}")
        super().display_info()       # call parent method
        print(f"  Specialization : {self.__specialization}")
        print(f"  Phone          : {self.__phone}")
        subjects_str = ", ".join(self.__subjects) if self.__subjects else "None"
        print(f"  Subjects       : {subjects_str}")

    # ── JSON Serialization ────────────────────────────────────

    def to_dict(self) -> dict:
        """Converts the teacher to a dictionary for JSON saving."""
        data = super().to_dict()
        data["type"]           = "teacher"
        data["specialization"] = self.__specialization
        data["phone"]          = self.__phone
        data["subjects"]       = self.__subjects
        return data

    @staticmethod
    def from_dict(data: dict) -> "Teacher":
        """Recreates a Teacher object from a dictionary."""
        t = Teacher(
            data["id"], data["last_name"], data["first_name"], data["email"],
            data["specialization"], data["phone"]
        )
        t._Teacher__subjects = data.get("subjects", [])
        return t
        
