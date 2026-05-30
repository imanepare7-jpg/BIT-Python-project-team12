"""
constants.py
------------
Global constants used throughout the project.
"""

# JSON data file name
DATA_FILE = "school_data.json"

# School name
SCHOOL_NAME = "Burkina Institute of Technology"

# Minimum passing grade
PASSING_GRADE = 10.0

# Tuple of grade mentions (immutable — never changes)
MENTIONS = (
    "Fail",
    "Pass",
    "Satisfactory",
    "Good",
    "Very Good",
    "Excellent"
)

# Tuple of corresponding score thresholds
MENTION_THRESHOLDS = (0, 10, 12, 14, 16, 18)

