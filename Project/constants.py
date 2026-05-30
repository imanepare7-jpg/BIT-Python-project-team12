"""
constants.py
------------
Global constants used throughout the project.
"""

# JSON data file name
DATA_FILE: str = "school_data.json"

# School name
SCHOOL_NAME: str = "Burkina Institute of Technology"

# Minimum passing grade
PASSING_GRADE: float = 10.0

# Tuple of grade mentions (immutable — never changes)
MENTIONS: tuple = (
    "Fail",
    "Pass",
    "Satisfactory",
    "Good",
    "Very Good",
    "Excellent"
)

# Tuple of corresponding score thresholds
MENTION_THRESHOLDS: tuple = (0, 10, 12, 14, 16, 18)

