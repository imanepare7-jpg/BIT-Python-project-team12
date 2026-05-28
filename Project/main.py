# ── Imports ──────────────────────────────────────────────────
from school      import School
from menus      import main_menu
from constants  import SCHOOL_NAME
from models     import Student, Teacher  


# ── Main Function ───────────────────────────────────────

def main():
    school = School(SCHOOL_NAME)
    school.load()          
    main_menu(school) 


# ── Execution ─────────────────────────────────────────────────
if __name__ == "__main__":
    main()
