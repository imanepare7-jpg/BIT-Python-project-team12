#HumanBF is the class that other must heritate
class Person:
    """
    Classe parente représentant une personne.
    Sert de base pour Etudiant et Professeur (héritage).
    Démontre : encapsulation, abstraction.
    """

    def __init__(self, id: str, nom: str, prenom: str, email: str):
        """
        Constructeur de Person.
        :param id: identifiant unique
        :param nom: nom de famille
        :param prenom: prénom
        :param email: adresse email
        """
        self.__id     = id        # attribut privé (encapsulation)
        self.__nom    = nom
        self.__prenom = prenom
        self.__email  = email

    # ── Getters (encapsulation) ──────────────────────────────

    def get_id(self) -> str:
        """Retourne l'identifiant."""
        return self.__id

    def get_nom(self) -> str:
        """Retourne le nom."""
        return self.__nom

    def get_prenom(self) -> str:
        """Retourne le prénom."""
        return self.__prenom

    def get_email(self) -> str:
        """Retourne l'email."""
        return self.__email

    def get_nom_complet(self) -> str:
        """Retourne le nom complet (prénom + nom)."""
        return f"{self.__prenom} {self.__nom}"

    # ── Méthodes ─────────────────────────────────────────────

    def afficher_info(self):
        """
        Affiche les informations de base.
        Redéfinie dans Etudiant et Professeur (polymorphisme).
        """
        print(f"  ID     : {self.__id}")
        print(f"  Nom    : {self.get_nom_complet()}")
        print(f"  Email  : {self.__email}")

    def to_dict(self) -> dict:
        """Convertit l'objet en dictionnaire pour la sauvegarde JSON."""
        return {
            "id":     self.__id,
            "nom":    self.__nom,
            "prenom": self.__prenom,
            "email":  self.__email
        }
