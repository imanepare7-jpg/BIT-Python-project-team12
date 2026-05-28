"""
models/etudiant.py
------------------
Contient la classe Etudiant qui hérite de Person.
"""

from models.Human  import Person
from constants      import PASSING_GRADE, MENTIONS, SEUILS_MENTIONS


class Etudiant(Person):
    """
    Représente un étudiant. Hérite de Person.
    Ajoute : classe, date de naissance, notes, absences.
    Démontre : héritage, encapsulation, polymorphisme.
    """

    def __init__(self, id: str, nom: str, prenom: str, email: str,
                 classe: str, date_naissance: str):
        """
        Constructeur de Etudiant.
        :param classe: classe de l'étudiant (ex: L1, L2)
        :param date_naissance: date de naissance (JJ/MM/AAAA)
        """
        super().__init__(id, nom, prenom, email)   # appel du constructeur parent
        self.__classe          = classe
        self.__date_naissance  = date_naissance
        self.__notes: dict     = {}   # {matiere: [note1, note2, ...]}
        self.__absences: list  = []   # [{"date": ..., "matiere": ...}]

    # ── Getters ──────────────────────────────────────────────

    def get_classe(self) -> str:
        """Retourne la classe de l'étudiant."""
        return self.__classe

    def get_notes(self) -> dict:
        """Retourne le dictionnaire des notes."""
        return self.__notes

    def get_absences(self) -> list:
        """Retourne la liste des absences."""
        return self.__absences

    def get_nombre_absences(self) -> int:
        """Retourne le nombre total d'absences."""
        return len(self.__absences)

    # ── Notes & Moyennes ─────────────────────────────────────

    def ajouter_note(self, matiere: str, note: float):
        """
        Ajoute une note pour une matière donnée.
        :param matiere: nom de la matière
        :param note: note entre 0 et 20
        """
        if matiere not in self.__notes:
            self.__notes[matiere] = []
        self.__notes[matiere].append(note)

    def get_moyenne_matiere(self, matiere: str) -> float:
        """
        Calcule la moyenne pour une matière.
        :param matiere: nom de la matière
        :return: moyenne ou 0.0 si aucune note
        """
        if matiere in self.__notes and len(self.__notes[matiere]) > 0:
            # Opérations arithmétiques : somme / nombre
            return sum(self.__notes[matiere]) / len(self.__notes[matiere])
        return 0.0

    def get_moyenne_generale(self) -> float:
        """Calcule la moyenne générale sur toutes les matières."""
        if not self.__notes:
            return 0.0
        moyennes = [self.get_moyenne_matiere(m) for m in self.__notes]
        return sum(moyennes) / len(moyennes)

    def est_admis(self) -> bool:
        """Retourne True si la moyenne générale >= note de passage."""
        return self.get_moyenne_generale() >= PASSING_GRADE

    def get_mention(self) -> str:
        """
        Retourne la mention correspondant à la moyenne.
        Utilise les tuples MENTIONS et SEUILS_MENTIONS.
        """
        moyenne: float = self.get_moyenne_generale()
        mention_actuelle: str = MENTIONS[0]   # "Insuffisant" par défaut
        for i in range(len(SEUILS_MENTIONS)):
            if moyenne >= SEUILS_MENTIONS[i]:
                mention_actuelle = MENTIONS[i]
        return mention_actuelle

    # ── Absences ─────────────────────────────────────────────

    def ajouter_absence(self, date: str, matiere: str):
        """
        Enregistre une absence.
        :param date: date de l'absence (JJ/MM/AAAA)
        :param matiere: matière concernée
        """
        self.__absences.append({"date": date, "matiere": matiere})

    # ── Affichage (polymorphisme) ─────────────────────────────

    def afficher_info(self):
        """
        Affiche les informations complètes de l'étudiant.
        Redéfinit la méthode de Person — polymorphisme.
        """
        print(f"\n{'='*45}")
        print(f"  ETUDIANT : {self.get_nom_complet()}")
        print(f"{'='*45}")
        super().afficher_info()     # appel de la méthode parente
        print(f"  Classe   : {self.__classe}")
        print(f"  Naissance: {self.__date_naissance}")
        print(f"  Absences : {self.get_nombre_absences()}")
        moy    = self.get_moyenne_generale()
        statut = "ADMIS ✓" if self.est_admis() else "NON ADMIS ✗"
        print(f"  Moyenne  : {moy:.2f}/20  ({statut})")
        print(f"  Mention  : {self.get_mention()}")

    # ── Sérialisation JSON ────────────────────────────────────

    def to_dict(self) -> dict:
        """Convertit l'étudiant en dictionnaire pour sauvegarde JSON."""
        data = super().to_dict()
        data["type"]            = "etudiant"
        data["classe"]          = self.__classe
        data["date_naissance"]  = self.__date_naissance
        data["notes"]           = self.__notes
        data["absences"]        = self.__absences
        return data

    @staticmethod
    def from_dict(data: dict) -> "Etudiant":
        """Recrée un objet Etudiant depuis un dictionnaire (chargement fichier)."""
        e = Etudiant(
            data["id"], data["nom"], data["prenom"], data["email"],
            data["classe"], data["date_naissance"]
        )
        e._Etudiant__notes    = data.get("notes", {})
        e._Etudiant__absences = data.get("absences", [])
        return e
