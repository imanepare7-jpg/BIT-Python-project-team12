"""
main.py
-------
Main entry point of the School Management System.
Run with: python main.py

Project structure:
    main.py         -> Entry point
    constants.py    -> Global constants
    school.py       -> School class (central manager)
    utils.py        -> Utility functions
    menus.py        -> All menus (user interface)
    models/
        __init__.py     -> Package initializer
        person.py       -> Parent class Person
        student.py      -> Student class (inherits from Person)
        teacher.py      -> Teacher class (inherits from Person)
        subject.py      -> Subject class
"""

# ── Imports ──────────────────────────────────────────────────
from school    import School
from menus     import main_menu
from constants import SCHOOL_NAME
from models    import Student, Teacher    # import from the models package


    # Explicit creation of 2 Student objects (inheriting from Person)
    student1 = Student("DEM001", "Kabore", "Alice",
                       "alice@bit.bf", "L1", "01/01/2004")
    student2 = Student("DEM002", "Traore", "Bob",
                       "bob@bit.bf",  "L1", "05/06/2003")

    # Grade lists + for loop
    grades_alice: list = [14.0, 16.0, 12.0]
    grades_bob:   list = [8.0,  9.5,  7.0]

    for grade in grades_alice:
        student1.add_grade("Mathematics", grade)
    for grade in grades_bob:
        student2.add_grade("Mathematics", grade)

    # Explicit arithmetic operations
    sum_alice:    float = sum(grades_alice)              # 42.0
    avg_alice:    float = sum_alice / len(grades_alice)  # 14.0
    pass_rate:    float = (1 / 2) * 100                  # 50%

    print(f"\n  Sum of Alice's grades : {sum_alice}")
    print(f"  Alice's average       : {avg_alice:.2f}/20")
    print(f"  Class pass rate       : {pass_rate:.0f}%")
    print(f"  Alice's mention       : {student1.get_mention()}")
    print(f"  Bob's mention         : {student2.get_mention()}")

    # Explicit creation of a Teacher object (inheriting from Person)
    teacher1 = Teacher("DEM_T01", "Blebo", "Kweyakie",
                       "blebo@bit.bf", "Computer Science", "+226 00 00 00")
    teacher1.add_subject("Mathematics")

    # POLYMORPHISM — same method name, DIFFERENT behavior
    print("\n  --- Polymorphism: display_info() ---")
    student1.display_info()   # Student version
    teacher1.display_info()   # Teacher version

    print("\n  [Demonstration complete]\n")


# ── Main Function ─────────────────────────────────────────────

def main():
    """
    Main function — creates the school, loads data, launches menus.
    """
    school = School(SCHOOL_NAME)   # create the School object
    school.load()                  # load existing data from JSON
    main_menu(school)              # launch the user interface


# ── Entry Point ───────────────────────────────────────────────
if __name__ == "__main__":
    main()

  
