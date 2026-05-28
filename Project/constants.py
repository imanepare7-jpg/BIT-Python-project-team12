"""
constants.py
------------
Contains all global constants used in the project. 
"""

# Data backup file
DATA_FILE: str = "school_data.json"

# School name
SCHOOL_NAME: str = "Burkina Institute of Technology"

# minimum grade to pass
PASSING_GRADE: float = 10.0

# Tuple of grades (immutable — never changes)
MENTIONS: tuple = (
    "fail",
    "Pass",
    "Fairly Good",
    "Good",
    "Very Good",
    "Excellent"
)

# Tuple of thresholds corresponding to the mentions
SEUILS_MENTIONS: tuple = (0, 10, 12, 14, 16, 18)
