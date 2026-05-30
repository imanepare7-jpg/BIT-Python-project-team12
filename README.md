SCHOOL MANAGEMENT SYSTEM
This project is a complete school management system that allows a school administration to easily manage its data: student enrollment, teacher registration, grade tracking, report card generation, absence recording, and class statistics. All data is automatically saved in a JSON file and reloaded every time the program starts.

HOW TO RUN THE PROGRAMM

Requirements
  Python 3.8 or higher
  No external libraries required (standard modules only)

Steps

1. Clone the repository
git clone https://github.com/imanepare7-jpg/BIT-Python-project-team12.git

2. Go into the project folder
cd BIT-Python-project-team12

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

## OOP Structure

| Class | File | Inherits From | Key Methods |
|-------|------|---------------|-------------|
| Person | models/person.py | - | get_full_name(), display_info() |
| Student | models/student.py | Person | add_grade(), get_overall_average(), get_mention() |
| Teacher | models/teacher.py | Person | add_subject(), display_info() |
| Subject | models/subject.py | - | set_teacher(), display_info() |
| School | school.py | - | add_student(), generate_report_card(), save(), load() |

## The 4 OOP Principles

| Principle | How it is implemented |
|-----------|----------------------|
| Encapsulation | Class attributes are private and accessed only through getters |
| Abstraction | The School class hides complexity behind simple methods |
| Inheritance | Student and Teacher both inherit from Person |
| Polymorphism | display_info() behaves differently in Student and Teacher |


GROUP MEMBERS 

| Name              | GitHub                     | Contribution |
| Member 1          | [@github](https://github.com/) | Person class, Student class |
| Member 2          | [@github](https://github.com/) | Teacher class, Subject class |
| Member 3          | [@github](https://github.com/) | School class (save/load, statistics) |
| Member 4          | [@github](https://github.com/) | Student & Teacher menus |
| OUEDRAOGO Oumarou |(https://github.com/omar04ryoued-cmyk) | school.py, person.py, README ,__init__.py|







