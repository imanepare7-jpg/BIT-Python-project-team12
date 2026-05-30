from models.person import Person

class Teacher(Person):
    def __init__(self, id, last_name, first_name, email,
                 specialization, phone):
        """
        Constructor for Teacher.
        """
        super().__init__(id, last_name, first_name, email)  # parent constructor
        self.specialization = specialization
        self.phone = phone
        self.subjects: list = []

    def get_specialization(self) -> str:
        """Returns the teacher's specialization."""
        return self.specialization
        
    def get_phone(self) -> str:
        """Returns the phone number."""
        return self.phone
        
    def get_subjects(self) -> list:
        """Returns the list of subjects taught."""
        return self.subjects

    def add_subject(self, subject: str):
        """Adds a subject to the list if not already present."""
        if subject not in self.__subjects:
            self.subjects.append(subject)

    def to_dict(self) -> dict:
        """Converts the teacher to a dictionary for JSON saving."""
        data = super().to_dict()
        data["type"] = "teacher"
        data["specialization"] = self.specialization
        data["phone"] = self.phone
        data["subjects"] = self.subjects
        return data
        
    @staticmethod
    def from_dict(data: dict) -> "Teacher":
        """Recreates a Teacher object from a dictionary."""
        t = Teacher(
            data["id"], data["last_name"], data["first_name"], data["email"],
            data["specialization"], data["phone"]
        )
        t._eacher__subjects = data.get("subjects", [])
        return t

    def display_info(self):
        """
        Displays full teacher information.
        Overrides the Person method — polymorphism.
        """
        print(f"\n{'='*45}")
        print(f"  TEACHER  : {self.get_full_name()}")
        print(f"{'='*45}")
        super().display_info()       # call parent method
        print(f"  Specialization : {self.specialization}")
        print(f"  Phone : {self.phone}")
        subjects_str = ", ".join(self.subjects) if self.subjects else "None"
        print(f"  Subjects : {subjects_str}")

    def to_dict(self) -> dict:
        """Converts the teacher to a dictionary for JSON saving."""
        data = super().to_dict()
        data["type"] = "teacher"
        data["specialization"] = self.specialization
        data["phone"]  = self.phone
        data["subjects"]  = self.subjects
        return data

    @staticmethod
    def from_dict(data: dict) -> "Teacher":
        """Recreates a Teacher object from a dictionary."""
        t = Teacher(
            data["id"], data["last_name"], data["first_name"], data["email"],
            data["specialization"], data["phone"]
        )
        t.subjects = data.get("subjects", [])
        return t
        

    def display_info(self):
        """
        Displays full teacher information.
        Overrides the Person method — polymorphism.
        """
        print(f"\n{'='*45}")
        print(f"  TEACHER   : {self.get_full_name()}")
        print(f"{'='*45}")
        super().display_info()       # call parent method
        print(f"  Specialization : {self.specialization}")
        print(f"  Phone          : {self.phone}")
        subjects_str = ", ".join(self.subjects) if self.ubjects else "None"
        print(f"  Subjects       : {subjects_str}")


    def to_dict(self) -> dict:
        """Converts the teacher to a dictionary for JSON saving."""
        data = super().to_dict()
        data["type"]   = "teacher"
        data["specialization"] = self.specialization
        data["phone"]  = self.phone
        data["subjects"] = self.subjects
        return data

    @staticmethod
    def from_dict(data: dict) -> "Teacher":
        """Recreates a Teacher object from a dictionary."""
        t = Teacher(
            data["id"], data["last_name"], data["first_name"], data["email"],
            data["specialization"], data["phone"]
        )
        t.subjects = data.get("subjects", [])
        return t
        
