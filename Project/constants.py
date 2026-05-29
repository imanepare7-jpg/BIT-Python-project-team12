"""
constants.py
------------
Contient toutes les constantes globales utilisées dans le projet.
"""

# Fichier de sauvegarde des données
DATA_FILE: str = "school_data.json"

# Nom de l'école
SCHOOL_NAME: str = "Burkina Institute of Technology"

# Note minimale pour être admis
PASSING_GRADE: float = 10.0

# Tuple des mentions (immuable — ne change jamais)
MENTIONS: tuple = (
    "Insuffisant",
    "Passable",
    "Assez Bien",
    "Bien",
    "Très Bien",
    "Excellent"
)

# Tuple des seuils correspondants aux mentions
SEUILS_MENTIONS: tuple = (0, 10, 12, 14, 16, 18)

