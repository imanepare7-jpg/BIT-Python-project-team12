from school    import School
from menus     import main_menu
from constants import SCHOOL_NAME
from models    import Student, Teacher    # import from the models package


def main():
    # Main function — creates the school, loads data, launches menus.
    school = School(SCHOOL_NAME)   # create the School object
    school.load()                  # load existing data from JSON
    main_menu(school)              # launch the user interface

if __name__ == "__main__":
    main()


