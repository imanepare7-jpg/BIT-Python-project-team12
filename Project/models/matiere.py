"""
models/matiere.py
-----------------
Contient la classe Matiere représentant un cours.
"""


class Matiere:
    """
    Représente une matière / cours dans l'école.
    Attributs : code, nom, crédits, professeur assigné.
    """

    def __init__(self, code: str, nom: str, credits: int,
                 professeur_id: str = ""):
        """
        Constructeur de Matiere.
        :param code: code unique (ex: MATH101)
        :param nom: nom complet de la matière
        :param credits: nombre de crédits (int)
        :param professeur_id: ID du professeur assigné
        """
        self.__code          = code
        self.__nom           = nom
        self.__credits: int  = credits      # type int
        self.__professeur_id = professeur_id

    # ── Getters ──────────────────────────────────────────────

    def get_code(self) -> str:
        """Retourne le code de la matière."""
        return self.__code

    def get_nom(self) -> str:
        """Retourne le nom de la matière."""
        return self.__nom

    def get_credits(self) -> int:
        """Retourne le nombre de crédits."""
        return self.__credits

    def get_professeur_id(self) -> str:
        """Retourne l'ID du professeur assigné."""
        return self.__professeur_id

    # ── Setter ───────────────────────────────────────────────

    def set_professeur(self, prof_id: str):
        """Assigne un professeur à cette matière."""
        self.__professeur_id = prof_id

    # ── Affichage ────────────────────────────────────────────

    def afficher_info(self):
        """Affiche les informations de la matière."""
        prof = self.__professeur_id if self.__professeur_id else "Non assigné"
        print(f"  [{self.__code}] {self.__nom} — "
              f"{self.__credits} crédit(s) — Prof ID: {prof}")

    # ── Sérialisation JSON ────────────────────────────────────

    def to_dict(self) -> dict:
        """Convertit la matière en dictionnaire pour sauvegarde JSON."""
        return {
            "code":          self.__code,
            "nom":           self.__nom,
            "credits":       self.__credits,
            "professeur_id": self.__professeur_id
        }

    @staticmethod
    def from_dict(data: dict) -> "Matiere":
        """Recrée un objet Matiere depuis un dictionnaire."""
        return Matiere(
            data["code"],
            data["nom"],
            data["credits"],
            data.get("professeur_id", "")
        )
