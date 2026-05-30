SCHOOL MANAGEMENT SYSTEM

A command-line application built in Python to manage students, teachers, subjects, grades, and absences for a school.

DESCRIPTION

This project is a complete school management system that allows a school administration to easily manage its data: student enrollment, teacher registration, grade tracking, report card generation, absence recording, and class statistics. All data is automatically saved in a JSON file and reloaded every time the program starts.

HOW TO RUN THE PROGRAMM

Requirements
  Python 3.8 or higher
  No external libraries required (standard modules only)

Steps

1. Clone the repository
git clone https://github.com/imanepare7-jpg/BIT-Python-project-team12.git

2. Go into the project folder
cd BIT-Python-project-team12.git

3. Run the application
python main.py

FEATURE

-  Add, list, search, and delete students
-  Add, list, and manage teachers
-  Create and manage subjects with credits
-  Record grades for students per subject
-  Calculate subject and overall averages automatically
-  Generate a full report card for any student
-  Record absences per student per subject
-  Display class statistics (average, pass rate, highest/lowest grade)
-  Assign teachers to subjects
-  Automatic data saving to a JSON file
-  Automatic data loading at startup

PROJECT STRUCTURE

Project/
 main.py           # Entry point 
 constants.py      # Global constants 
 school.py         # School class
 utils.py          # Utility functions 
 menus.py          # All user interface menus
 school_data.json  # Auto-generated data file (created on first run)

 models/           
       __init__.py   # Package initializer
       person.py     # Person class — parent class (inheritance base)
       student.py    # Student class — inherits from Person
       teacher.py    # Teacher class — inherits from Person
       subject.py    # Subject class — represents a course


OOP STRUCTURE 

|--Class----|--File-----------|-Inherits From-|Key Methods--------------------------------
|--Person---|models/person.py-|---------------|get_full_name(),display_info(),to_dict()
| `Student` |models/student.py|--Person------ |add_grade(),get_overall_average(),is_passing(),get_mention(),add_absence()
| `Teacher` |models/teacher.py|--Person-------|add_subject(),get_subjects(),display_info()
| `Subject` |models/subject.py|---------------|set_teacher(),display_info(),to_dict()
| `School`  |school.py--------|---------------|add_student(),generate_report_card(),class_statistics(),save(),load()

### The 4 OOP Principles in This Project

| Principle | How it is implemented |
|---|---|
| **Encapsulation** | All class attributes are private (`__name`, `__grades`, etc.) and accessed only through getters |
| **Abstraction** | The `School` class hides all internal complexity behind simple methods like `add_student()` or `generate_report_card()` |
| **Inheritance** | `Student` and `Teacher` both inherit from `Person` using `super().__init__()` |
| **Polymorphism** | `display_info()` is defined in `Person` and overridden differently in `Student` and `Teacher` |

---





GROUP MEMBERS 

| Name              | GitHub                     | Contribution |
| Member 1 | [@github](https://github.com/) | Person class, Student class |
| Member 2 | [@github](https://github.com/) | Teacher class, Subject class |
| Member 3 | [@github](https://github.com/) | School class (save/load, statistics) |
| Member 4 | [@github](https://github.com/) | Student & Teacher menus |
| OUEDRAOGO Oumarou | [@github](https://github.com/) | school.py, person.py, README |







