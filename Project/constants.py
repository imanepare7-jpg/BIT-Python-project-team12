"""
constants.py
------------
Contient toutes les constantes globales utilisées dans le projet.
"""

# Fichier de sauvegarde des données
DATA_FILE: str = "school_data.json"

# School name
SCHOOL_NAME: str = "Burkina Institute of Technology"

# minimum grade to pass
PASSING_GRADE: float = 10.0

# Tuple of grades (immuable — ne change jamais)
MENTIONS: tuple = (
    "fail",
    "Pass",
    "Fairly Good",
    "Good",
    "Very Good",
    "Excellent"
)

# Tuple des seuils correspondants aux mentions
SEUILS_MENTIONS: tuple = (0, 10, 12, 14, 16, 18)
