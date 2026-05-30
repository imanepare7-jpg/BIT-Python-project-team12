# School Management System 

A command-line application built in Python to manage students, teachers, subjects, grades, and absences for a school.

## Description

This project is a complete school management system that allows a school administration to easily manage its data: student enrollment, teacher registration, grade tracking, report card generation, absence recording, and class statistics. All data is automatically saved in a JSON file and reloaded every time the program starts.


# 1. Clone the repository
git clone https://github.com/imanepare7-jpg/BIT-Python-project-team12.git

# 2. Go into the project folder
cd BIT-Python-project-team12.git

# 3. Run the application
python main.py

## Features

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


## Project Structure

school_project/
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


## Group Members

| Name              | GitHub                     | Contribution |
| Member 1 | [@github](https://github.com/) | Person class, Student class |
| Member 2 | [@github](https://github.com/) | Teacher class, Subject class |
| Member 3 | [@github](https://github.com/) | School class (save/load, statistics) |
| Member 4 | [@github](https://github.com/) | Student & Teacher menus |
| OUEDRAOGO Oumarou | [@github](https://github.com/) | school.py, person.py, README |






