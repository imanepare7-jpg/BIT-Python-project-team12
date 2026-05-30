"""
models/teacher.py
-----------------
Contains the Teacher class which inherits from Person.
"""

from models.person import Person


class Teacher(Person):
    """
    Represents a teacher. Inherits from Person.
    Adds: specialization, phone number, list of subjects taught.
    Demonstrates: inheritance, polymorphism.
    """
def __init__(self, id: str, last_name: str, first_name: str, email: str,
                 specialization: str, phone: str):
        """
        Constructor for Teacher.
        :param specialization: area of expertise
        :param phone: phone number
        """
        super().__init__(id, last_name, first_name, email)  # parent constructor
        self.__specialization = specialization
        self.__phone          = phone
        self.__subjects: list = []
