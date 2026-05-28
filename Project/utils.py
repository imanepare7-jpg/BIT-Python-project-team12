"""
utils.py
--------
Fonctions utilitaires réutilisables dans tous les menus.
Importées par menus.py et main.py
"""

import os


def effacer_ecran():
    """Efface le terminal selon le système d'exploitation."""
    os.system('cls' if os.name == 'nt' else 'clear')


def pause():
    """Met en pause et attend que l'utilisateur appuie sur Entrée."""
    input("\n  [Appuyez sur Entrée pour continuer...]")


def afficher_entete(nom_ecole: str):
    """
    Affiche l'en-tête principal de l'application.
    :param nom_ecole: nom de l'école à afficher
    """
    print("\n" + "="*55)
    print(f"   {nom_ecole}")
    print(f"   Système de Gestion Scolaire v1.0")
    print("="*55)


def lire_float(message: str, mini: float = 0, maxi: float = 20) -> float:
    """
    Lit un nombre décimal valide compris entre mini et maxi.
    Utilise une boucle while et gère les erreurs avec try/except.
    :param message: message affiché à l'utilisateur
    :param mini: valeur minimale acceptée
    :param maxi: valeur maximale acceptée
    :return: float valide
    """
    while True:
        try:
            valeur = float(input(message))      # conversion str -> float
            if mini <= valeur <= maxi:
                return valeur
            else:
                print(f"  [!] Entrez une valeur entre {mini} et {maxi}.")
        except ValueError:
            print("  [!] Veuillez entrer un nombre valide.")


def lire_entier(message: str, mini: int = 1) -> int:
    """
    Lit un entier valide >= mini.
    :param message: message affiché
    :param mini: valeur minimale acceptée
    :return: entier valide
    """
    while True:
        try:
            valeur = int(input(message))        # conversion str -> int
            if valeur >= mini:
                return valeur
            else:
                print(f"  [!] Entrez un nombre >= {mini}.")
        except ValueError:
            print("  [!] Veuillez entrer un nombre entier.")
