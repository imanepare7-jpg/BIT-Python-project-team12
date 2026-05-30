"""
models/professeur.py
--------------------
Contient la classe Professeur qui hérite de Person.
"""

from models.Human import Person


class Professeur(Person):
    """
    Représente un professeur. Hérite de Person.
    Ajoute : spécialité, téléphone, matières enseignées.
    Démontre : héritage, polymorphisme.
    """

    def __init__(self, id: str, nom: str, prenom: str, email: str,
                 specialite: str, telephone: str):
        """
        Constructeur de Professeur.
        :param specialite: domaine de spécialisation
        :param telephone: numéro de téléphone
        """
        super().__init__(id, nom, prenom, email)   # constructeur parent
        self.__specialite = specialite
        self.__telephone  = telephone
        self.__matieres: list = []    # liste des matières enseignées

    # ── Getters ──────────────────────────────────────────────

    def get_specialite(self) -> str:
        """Retourne la spécialité du professeur."""
        return self.__specialite

    def get_telephone(self) -> str:
        """Retourne le numéro de téléphone."""
        return self.__telephone

    def get_matieres(self) -> list:
        """Retourne la liste des matières enseignées."""
        return self.__matieres

    # ── Méthodes ─────────────────────────────────────────────

    def ajouter_matiere(self, matiere: str):
        """Ajoute une matière à la liste si elle n'y est pas déjà."""
        if matiere not in self.__matieres:
            self.__matieres.append(matiere)

    # ── Affichage (polymorphisme) ─────────────────────────────

    def afficher_info(self):
        """
        Affiche les informations du professeur.
        Redéfinit la méthode de Person — polymorphisme.
        """
        print(f"\n{'='*45}")
        print(f"  PROFESSEUR : {self.get_nom_complet()}")
        print(f"{'='*45}")
        super().afficher_info()    # appel de la méthode parente
        print(f"  Spécialité : {self.__specialite}")
        print(f"  Téléphone  : {self.__telephone}")
        matieres_str = ", ".join(self.__matieres) if self.__matieres else "Aucune"
        print(f"  Matières   : {matieres_str}")

    # ── Sérialisation JSON ────────────────────────────────────

    def to_dict(self) -> dict:
        """Convertit le professeur en dictionnaire pour sauvegarde JSON."""
        data = super().to_dict()
        data["type"]       = "professeur"
        data["specialite"] = self.__specialite
        data["telephone"]  = self.__telephone
        data["matieres"]   = self.__matieres
        return data

    @staticmethod
    def from_dict(data: dict) -> "Professeur":
        """Recrée un objet Professeur depuis un dictionnaire."""
        p = Professeur(
            data["id"], data["nom"], data["prenom"], data["email"],
            data["specialite"], data["telephone"]
        )
        p._Professeur__matieres = data.get("matieres", [])
        return p
