"""
menus.py
--------
Contains all user interface menus.
Imports School from school.py and utilities from utils.py
"""

import datetime

from school    import School
from utils     import clear_screen, pause, display_header, read_float, read_integer
from constants import SCHOOL_NAME


# ── Student Menu ──────────────────────────────────────────────

def student_menu(school: School):
    """Full student management menu."""
    while True:
        clear_screen()
        display_header(SCHOOL_NAME)
        print("\n  === STUDENT MANAGEMENT ===")
        print("  1. Add a student")
        print("  2. List all students")
        print("  3. View student details")
        print("  4. Search for a student")
        print("  5. Delete a student")
        print("  0. Back to main menu")
        print()
        choice = input("  Your choice: ").strip()

        if choice == "1":
            print("\n  -- NEW STUDENT --")
            last_name     = input("  Last name     : ").strip()
            first_name    = input("  First name    : ").strip()
            email         = input("  Email         : ").strip()
            class_level   = input("  Class/Year    : ").strip()
            date_of_birth = input("  Date of birth (DD/MM/YYYY): ").strip()
            if last_name and first_name:
                s = school.add_student(last_name, first_name, email,
                                       class_level, date_of_birth)
                school.save()
                print(f"\n  ✓ Student added successfully! ID: {s.get_id()}")
            else:
                print("  [!] Last name and first name are required.")
            pause()

        elif choice == "2":
            students = school.get_all_students()
            print(f"\n  -- ALL STUDENTS ({len(students)}) --")
            if not students:
                print("  No students registered.")
            else:
                print(f"  {'ID':<10} {'FULL NAME':<28} {'CLASS':<8} {'AVERAGE'}")
                print("  " + "-"*58)
                for s in students:
                    avg = s.get_overall_average()
                    print(f"  {s.get_id():<10} {s.get_full_name():<28} "
                          f"{s.get_class_level():<8} {avg:.2f}/20")
            pause()

        elif choice == "3":
            student_id = input("\n  Student ID: ").strip()
            s = school.get_student(student_id)
            if s:
                s.display_info()
            else:
                print("  [!] Student not found.")
            pause()

        elif choice == "4":
            term    = input("\n  Search by name: ").strip()
            results = school.search_student(term)
            print(f"\n  {len(results)} result(s) found:")
            for s in results:
                print(f"  - [{s.get_id()}] {s.get_full_name()} "
                      f"({s.get_class_level()})")
            pause()

        elif choice == "5":
            student_id = input("\n  Student ID to delete: ").strip()
            confirm    = input("  Confirm deletion? (y/n): ").strip().lower()
            if confirm == "y":
                if school.delete_student(student_id):
                    school.save()
                    print("  ✓ Student deleted.")
                else:
                    print("  [!] Student not found.")
            pause()

        elif choice == "0":
            break


# ── Teacher Menu ──────────────────────────────────────────────

def teacher_menu(school: School):
    """Full teacher management menu."""
    while True:
        clear_screen()
        display_header(SCHOOL_NAME)
        print("\n  === TEACHER MANAGEMENT ===")
        print("  1. Add a teacher")
        print("  2. List all teachers")
        print("  3. View teacher details")
        print("  4. Assign a subject to a teacher")
        print("  5. Delete a teacher")
        print("  0. Back to main menu")
        print()
        choice = input("  Your choice: ").strip()

        if choice == "1":
            print("\n  -- NEW TEACHER --")
            last_name      = input("  Last name       : ").strip()
            first_name     = input("  First name      : ").strip()
            email          = input("  Email           : ").strip()
            specialization = input("  Specialization  : ").strip()
            phone          = input("  Phone           : ").strip()
            if last_name and first_name:
                t = school.add_teacher(last_name, first_name, email,
                                       specialization, phone)
                school.save()
                print(f"\n  ✓ Teacher added! ID: {t.get_id()}")
            else:
                print("  [!] Last name and first name are required.")
            pause()

        elif choice == "2":
            teachers = school.get_all_teachers()
            print(f"\n  -- ALL TEACHERS ({len(teachers)}) --")
            if not teachers:
                print("  No teachers registered.")
            else:
                print(f"  {'ID':<10} {'FULL NAME':<28} {'SPECIALIZATION'}")
                print("  " + "-"*55)
                for t in teachers:
                    print(f"  {t.get_id():<10} {t.get_full_name():<28} "
                          f"{t.get_specialization()}")
            pause()

        elif choice == "3":
            teacher_id = input("\n  Teacher ID: ").strip()
            t = school.get_teacher(teacher_id)
            if t:
                t.display_info()
            else:
                print("  [!] Teacher not found.")
            pause()

        elif choice == "4":
            teacher_id   = input("\n  Teacher ID   : ").strip()
            t = school.get_teacher(teacher_id)
            if t:
                subject_code = input("  Subject code : ").strip().upper()
                sj = school.get_subject(subject_code)
                if sj:
                    t.add_subject(sj.get_name())
                    sj.set_teacher(teacher_id)
                    school.save()
                    print(f"  ✓ Subject '{sj.get_name()}' assigned to "
                          f"{t.get_full_name()}.")
                else:
                    print("  [!] Subject not found.")
            else:
                print("  [!] Teacher not found.")
            pause()

        elif choice == "5":
            teacher_id = input("\n  Teacher ID to delete: ").strip()
            confirm    = input("  Confirm? (y/n): ").strip().lower()
            if confirm == "y":
                if school.delete_teacher(teacher_id):
                    school.save()
                    print("  ✓ Teacher deleted.")
                else:
                    print("  [!] Teacher not found.")
            pause()

        elif choice == "0":
            break


# ── Subject Menu ──────────────────────────────────────────────

def subject_menu(school: School):
    """Full subject management menu."""
    while True:
        clear_screen()
        display_header(SCHOOL_NAME)
        print("\n  === SUBJECT MANAGEMENT ===")
        print("  1. Add a subject")
        print("  2. List all subjects")
        print("  3. Delete a subject")
        print("  0. Back to main menu")
        print()
        choice = input("  Your choice: ").strip()

        if choice == "1":
            print("\n  -- NEW SUBJECT --")
            code    = input("  Code (e.g. MATH101): ").strip().upper()
            name    = input("  Full name           : ").strip()
            credits = read_integer("  Credits             : ")
            if code and name:
                school.add_subject(code, name, credits)
                school.save()
                print(f"  ✓ Subject '{name}' added.")
            else:
                print("  [!] Code and name are required.")
            pause()

        elif choice == "2":
            subjects = school.get_all_subjects()
            print(f"\n  -- ALL SUBJECTS ({len(subjects)}) --")
            if not subjects:
                print("  No subjects registered.")
            else:
                for sj in subjects:
                    sj.display_info()
            pause()

        elif choice == "3":
            code    = input("\n  Subject code to delete: ").strip().upper()
            confirm = input("  Confirm? (y/n): ").strip().lower()
            if confirm == "y":
                if school.delete_subject(code):
                    school.save()
                    print("  ✓ Subject deleted.")
                else:
                    print("  [!] Subject not found.")
            pause()

        elif choice == "0":
            break


# ── Grades & Absences Menu ────────────────────────────────────

def grades_menu(school: School):
    """Grades, absences, report cards and class statistics menu."""
    while True:
        clear_screen()
        display_header(SCHOOL_NAME)
        print("\n  === GRADES & ABSENCES ===")
        print("  1. Add a grade to a student")
        print("  2. Record an absence")
        print("  3. View student report card")
        print("  4. Class statistics")
        print("  0. Back to main menu")
        print()
        choice = input("  Your choice: ").strip()

        if choice == "1":
            student_id   = input("\n  Student ID     : ").strip()
            subject_code = input("  Subject code   : ").strip().upper()
            grade        = read_float("  Grade (0 to 20): ", 0, 20)
            if school.add_grade(student_id, subject_code, grade):
                school.save()
                print(f"  ✓ Grade {grade} added successfully.")
            else:
                print("  [!] Student or subject not found.")
            pause()

        elif choice == "2":
            student_id   = input("\n  Student ID     : ").strip()
            subject_code = input("  Subject code   : ").strip().upper()
            date         = input("  Date (DD/MM/YYYY): ").strip()
            if not date:
                date = datetime.date.today().strftime("%d/%m/%Y")
            if school.record_absence(student_id, subject_code, date):
                school.save()
                print("  ✓ Absence recorded.")
            else:
                print("  [!] Student or subject not found.")
            pause()

        elif choice == "3":
            student_id = input("\n  Student ID: ").strip()
            school.generate_report_card(student_id)
            pause()

        elif choice == "4":
            class_level = input("\n  Class/Year (e.g. L1): ").strip()
            school.class_statistics(class_level)
            pause()

        elif choice == "0":
            break


# ── Main Menu ─────────────────────────────────────────────────

def main_menu(school: School):
    """Main menu — entry point for navigation."""
    while True:
        clear_screen()
        display_header(SCHOOL_NAME)

        # Display counters
        nb_s  = len(school.get_all_students())
        nb_t  = len(school.get_all_teachers())
        nb_sj = len(school.get_all_subjects())
        print(f"\n  Students: {nb_s}  |  Teachers: {nb_t}  |  Subjects: {nb_sj}")

        print("\n  === MAIN MENU ===\n")
        print("  1. Student Management")
        print("  2. Teacher Management")
        print("  3. Subject Management")
        print("  4. Grades & Absences & Report Cards")
        print("  0. Quit")
        print()
        choice = input("  Your choice: ").strip()

        if choice == "1":
            student_menu(school)
        elif choice == "2":
            teacher_menu(school)
        elif choice == "3":
            subject_menu(school)
        elif choice == "4":
            grades_menu(school)
        elif choice == "0":
            school.save()
            print("\n  Goodbye! Data saved.\n")
            break
        else:
            print("  [!] Invalid choice. Please try again.")
            pause()
