
def students():
    while True:
        print("Burkina Institute of Technology")
        print("\n  === Students Manegements ===")
        print("  1. Add Students")
        print("  2. Students List")
        print("  3. View students informations")
        print("  4. Search Students")
        print("  5. Delete Students")
        print("  0. Return toMain Menu")
        print()
        choice = input("  Your choice : ")

        if choice == "1":
            # Add a students
            pass
        elif choice == "2":

             # Students List

            pass
        elif choice == "3":
            # View students informations
                pass

        elif choice == "4":

            # Search Students

            pass
        elif choice == "5":

            # Delete Students
            pass

        elif choice == "0":
            break

        else:
            print("  Invalid choice. Please try again.")



def teachers():
   
    while True:
        print("Burkina Institute of Technology")
        print("\n  === Teachers Management ===")
        print("  1. Add Teacher")
        print("  2. List All Teachers")
        print("  3. View Teacher Details")
        print("  4. Assign Subject to Teacher")
        print("  5. Delete Teacher")
        print("  0. Return to Main Menu")
        print()
        choice = input("  Your choice : ")

        if choice == "1":
            # Add a teacher
            pass
        elif choice == "2":

            # List All Teachers
            pass
        elif choice == "3":
            # View Teacher Details
            pass

        elif choice == "4":

            # Assign Subject to Teacher
            pass
        elif choice == "5":

            # Delete Teacher

            pass
        elif choice == "0":
            break

        else:
            print("  Invalid choice. Please try again.")
        

def Administrators():
    while True:
        print("Burkina Institute of Technology")
        print("\n  === Subjects management ===")
        print("  1. Add Administrator")
        print("  2. View Administrator details")
        print("  3. Delete Administrator")
        print("  0. Return to Main Menu")
        print()
        choice = input("  Your choice : ")

        if choice == "1":
            # Add a subject
            pass
        elif choice == "2":
            # View subject details
            pass
        elif choice == "3":
            # Delete Subject
            pass
        elif choice == "0":
            break
        else:
            print("  Invalid choice. Please try again.")



def studentsMarks():
    
    while True:
        print("Burkina Institute of Technology")
        print("\n  === Marks & ABSENCES & BULLETINS ===")
        print("  1. Add marks for a student")
        print("  2. Register an absence")
        print("  3. View a student's transcript")
        print("  4. Class statistics")
        print("  0. Return to main menu")
        print()
        choice = input("  Your choice : ")

        if choice == "1":
            # Add marks for a student
            pass
        elif choice == "2":
            # Register an absence
            pass
        elif choice == "3":
            # View a student's transcript
            pass
        elif choice == "4":
            # Class statistics
            pass
        elif choice == "0":
            break
        else:
            print("  Invalid choice. Please try again.")

def main():
    while True:
        print("Burkina Institute of Technology")

        print("\n  === Main Menu ===\n")
        print("  1. Students Management")
        print("  2. Teachers Management")
        print("  3. Administator Management")
        print("  4. Marks & Absences & Transcripts")
        print("  0. Quit")
        print()
        choice = input("  Your choice : ")

        if choice == "1":
            # Students Management
            pass
        elif choice == "2":
            # Teachers Management
            pass
        elif choice == "3":
            # Subjects Management
            pass
        elif choice == "4":
            # Marks & Absences & Transcripts
            pass
        elif choice == "0":
            break
        else:
            print("  Invalid choice. Please try again.")


