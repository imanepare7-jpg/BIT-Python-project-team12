
import os
import json
import datetime
from typing import Optional

from models.student import Student
from models.teacher import Teacher
from models.subject import Subject
from constants      import DATA_FILE, PASSING_GRADE


class School:
    """
    Main class that manages all students, teachers and subjects.
    Abstraction: hides complexity behind simple methods.
    """

    def __init__(self, name: str):
        """
        Constructor for School.
        :param name: school name
        """
        self.__name                  = name
        self.__students: dict        = {}   # {id: Student}
        self.__teachers: dict        = {}   # {id: Teacher}
        self.__subjects: dict        = {}   # {code: Subject}
        self.__student_counter: int  = 1
        self.__teacher_counter: int  = 1

    def get_name(self) -> str:
        """Returns the school name."""
        return self.__name

    # ── Student Management ────────────────────────────────────

    def add_student(self, last_name: str, first_name: str, email: str,
                    class_level: str, date_of_birth: str) -> Student:
        """
        Creates and adds a new student with an automatic ID.
        :return: the created Student object
        """
        student_id = f"STU{self.__student_counter:04d}"
        self.__student_counter += 1      # arithmetic operation
        student = Student(student_id, last_name, first_name,
                          email, class_level, date_of_birth)
        self.__students[student_id] = student
        return student

    def get_student(self, id: str) -> Optional[Student]:
        """Returns a student by ID, or None if not found."""
        return self.__students.get(id)

    def get_all_students(self) -> list:
        """Returns the list of all students."""
        return list(self.__students.values())

    def delete_student(self, id: str) -> bool:
        """Deletes a student. Returns True if successful."""
        if id in self.__students:
            del self.__students[id]
            return True
        return False

    def search_student(self, term: str) -> list:
        """Searches for a student by last or first name (case insensitive)."""
        term = term.lower()
        return [
            s for s in self.__students.values()
            if term in s.get_last_name().lower() or term in s.get_first_name().lower()
        ]

    # ── Teacher Management ────────────────────────────────────

    def add_teacher(self, last_name: str, first_name: str, email: str,
                    specialization: str, phone: str) -> Teacher:
        """Creates and adds a new teacher."""
        teacher_id = f"TCH{self.__teacher_counter:03d}"
        self.__teacher_counter += 1
        teacher = Teacher(teacher_id, last_name, first_name,
                          email, specialization, phone)
        self.__teachers[teacher_id] = teacher
        return teacher

    def get_teacher(self, id: str) -> Optional[Teacher]:
        """Returns a teacher by ID."""
        return self.__teachers.get(id)

    def get_all_teachers(self) -> list:
        """Returns the list of all teachers."""
        return list(self.__teachers.values())

    def delete_teacher(self, id: str) -> bool:
        """Deletes a teacher. Returns True if successful."""
        if id in self.__teachers:
            del self.__teachers[id]
            return True
        return False

    # ── Subject Management ────────────────────────────────────

    def add_subject(self, code: str, name: str, credits: int) -> Subject:
        """Creates and adds a new subject."""
        subject = Subject(code, name, credits)
        self.__subjects[code] = subject
        return subject

    def get_subject(self, code: str) -> Optional[Subject]:
        """Returns a subject by its code."""
        return self.__subjects.get(code)

    def get_all_subjects(self) -> list:
        """Returns the list of all subjects."""
        return list(self.__subjects.values())

    def delete_subject(self, code: str) -> bool:
        """Deletes a subject. Returns True if successful."""
        if code in self.__subjects:
            del self.__subjects[code]
            return True
        return False

    # ── Grades & Absences ─────────────────────────────────────

    def add_grade(self, student_id: str, subject_code: str,
                  grade: float) -> bool:
        """
        Adds a grade to a student for a subject.
        :return: True if successful, False otherwise
        """
        student = self.get_student(student_id)
        subject = self.get_subject(subject_code)
        if student and subject:
            student.add_grade(subject.get_name(), grade)
            return True
        return False

    def record_absence(self, student_id: str, subject_code: str,
                       date: str) -> bool:
        """Records an absence for a student in a subject."""
        student = self.get_student(student_id)
        subject = self.get_subject(subject_code)
        if student and subject:
            student.add_absence(date, subject.get_name())
            return True
        return False

    # ── Report Card ───────────────────────────────────────────

    def generate_report_card(self, student_id: str):
        """
        Generates and displays a student's report card.
        :param student_id: student ID
        """
        student = self.get_student(student_id)
        if not student:
            print("  [!] Student not found.")
            return

        today = datetime.date.today().strftime("%d/%m/%Y")
        print(f"\n{'#'*52}")
        print(f"  {self.__name}")
        print(f"  REPORT CARD")
        print(f"{'#'*52}")
        print(f"  Student  : {student.get_full_name()}")
        print(f"  ID       : {student.get_id()}")
        print(f"  Class    : {student.get_class_level()}")
        print(f"  Date     : {today}")
        print(f"{'-'*52}")
        print(f"  {'SUBJECT':<25} {'GRADES':<15} {'AVG':>6}")
        print(f"{'-'*52}")

        grades = student.get_grades()
        if not grades:
            print("  No grades recorded yet.")
        else:
            for subject, grade_list in grades.items():
                # Arithmetic operations
                avg        = sum(grade_list) / len(grade_list)
                grades_str = ", ".join([str(g) for g in grade_list])
                status     = "✓" if avg >= PASSING_GRADE else "✗"
                print(f"  {subject:<25} {grades_str:<15} {avg:>5.2f} {status}")

        print(f"{'-'*52}")
        overall  = student.get_overall_average()
        status   = "PASSING" if student.is_passing() else "FAILING"
        mention  = student.get_mention()
        print(f"  OVERALL AVERAGE  : {overall:.2f}/20")
        print(f"  MENTION          : {mention}")
        print(f"  STATUS           : {status}")
        print(f"  ABSENCES         : {student.get_absence_count()} absence(s)")
        print(f"{'#'*52}\n")

    # ── Statistics ────────────────────────────────────────────

    def class_statistics(self, class_level: str):
        """Displays statistics for a given class."""
        students = [
            s for s in self.__students.values()
            if s.get_class_level() == class_level
        ]
        if not students:
            print(f"  [!] No students found in class {class_level}.")
            return

        averages  = [s.get_overall_average() for s in students]
        passing   = [s for s in students if s.is_passing()]

        # Arithmetic operations
        class_avg     = sum(averages) / len(averages)
        highest_grade = max(averages)
        lowest_grade  = min(averages)
        pass_rate     = (len(passing) / len(students)) * 100

        print(f"\n{'='*52}")
        print(f"  CLASS STATISTICS — {class_level}")
        print(f"{'='*52}")
        print(f"  Total students   : {len(students)}")
        print(f"  Class average    : {class_avg:.2f}/20")
        print(f"  Highest grade    : {highest_grade:.2f}/20")
        print(f"  Lowest grade     : {lowest_grade:.2f}/20")
        print(f"  Pass rate        : {len(passing)}/{len(students)} ({pass_rate:.1f}%)")
        print(f"{'='*52}\n")

    # ── Save / Load ───────────────────────────────────────────

    def save(self):
        """Saves all data to the JSON file."""
        data = {
            "name":            self.__name,
            "student_counter": self.__student_counter,
            "teacher_counter": self.__teacher_counter,
            "students": [s.to_dict() for s in self.__students.values()],
            "teachers": [t.to_dict() for t in self.__teachers.values()],
            "subjects": [s.to_dict() for s in self.__subjects.values()],
        }
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def load(self):
        """Loads data from the JSON file at startup."""
        if not os.path.exists(DATA_FILE):
            return
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.__student_counter = data.get("student_counter", 1)
        self.__teacher_counter = data.get("teacher_counter", 1)

        for sd in data.get("students", []):
            s = Student.from_dict(sd)
            self.__students[s.get_id()] = s

        for td in data.get("teachers", []):
            t = Teacher.from_dict(td)
            self.__teachers[t.get_id()] = t

        for sjd in data.get("subjects", []):
            sj = Subject.from_dict(sjd)
            self.__subjects[sj.get_code()] = sj
