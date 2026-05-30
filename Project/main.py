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


