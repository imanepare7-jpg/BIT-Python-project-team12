
import datetime

from Project.school  import Ecole
from utils  import effacer_ecran, pause, afficher_entete, lire_float, lire_entier
from constants import SCHOOL_NAME


# ── Menu Etudiants ────────────────────────────────────────────

def menu_etudiants(ecole: Ecole):

    while True:
        effacer_ecran()
        afficher_entete(SCHOOL_NAME)
        print("\n  === GESTION DES ETUDIANTS ===")
        print("  1. Add a new student")
        print("  2. Lister tous les étudiants")
        print("  3. Voir les détails d'un étudiant")
        print("  4. Rechercher un étudiant")
        print("  5. Supprimer un étudiant")
        print("  0. Retour au menu principal")
        print()
        choix = input("  Votre choix : ").strip()

        if choix == "1":
            # Ajouter un étudiant
            print("\n  -- NEW STUDENTS --")
            nom    = input("  NAME         : ").strip()
            prenom = input("  Prénom      : ").strip()
            email  = input("  Email       : ").strip()
            classe = input("  Classe      : ").strip()
            dob    = input("  Date naiss. (JJ/MM/AAAA) : ").strip()
            if nom and prenom:
                e = ecole.ajouter_etudiant(nom, prenom, email, classe, dob)
                ecole.sauvegarder()
                print(f"\n  ✓ Étudiant ajouté avec succès ! ID : {e.get_id()}")
            else:
                print("  [!] Nom et prénom obligatoires.")
            pause()

        elif choix == "2":
            # Lister tous les étudiants
            etudiants = ecole.get_tous_etudiants()
            print(f"\n  -- LISTE DES ETUDIANTS ({len(etudiants)}) --")
            if not etudiants:
                print("  Aucun étudiant enregistré.")
            else:
                print(f"  {'ID':<10} {'NOM COMPLET':<25} {'CLASSE':<8} {'MOYENNE'}")
                print("  " + "-"*55)
                for e in etudiants:
                    moy = e.get_moyenne_generale()
                    print(f"  {e.get_id():<10} {e.get_nom_complet():<25} "
                          f"{e.get_classe():<8} {moy:.2f}/20")
            pause()

        elif choix == "3":
            # Détails d'un étudiant
            id_e = input("\n  ID de l'étudiant : ").strip()
            e = ecole.get_etudiant(id_e)
            if e:
                e.afficher_info()
            else:
                print("  [!] Étudiant non trouvé.")
            pause()

        elif choix == "4":
            # Recherche par nom/prénom
            terme     = input("\n  Nom ou prénom à rechercher : ").strip()
            resultats = ecole.rechercher_etudiant(terme)
            print(f"\n  {len(resultats)} résultat(s) trouvé(s) :")
            for e in resultats:
                print(f"  - [{e.get_id()}] {e.get_nom_complet()} "
                      f"({e.get_classe()})")
            pause()

        elif choix == "5":
            # Supprimer un étudiant
            id_e    = input("\n  ID de l'étudiant à supprimer : ").strip()
            confirm = input("  Confirmer la suppression ? (o/n) : ").strip().lower()
            if confirm == "o":
                if ecole.supprimer_etudiant(id_e):
                    ecole.sauvegarder()
                    print("  ✓ Étudiant supprimé.")
                else:
                    print("  [!] Étudiant non trouvé.")
            pause()

        elif choix == "0":
            break


# ── Menu Professeurs ──────────────────────────────────────────

def menu_professeurs(ecole: Ecole):
    """Menu complet de gestion des professeurs."""
    while True:
        effacer_ecran()
        afficher_entete(SCHOOL_NAME)
        print("\n  === GESTION DES PROFESSEURS ===")
        print("  1. Ajouter un professeur")
        print("  2. Lister tous les professeurs")
        print("  3. Voir les détails d'un professeur")
        print("  4. Assigner une matière à un professeur")
        print("  5. Supprimer un professeur")
        print("  0. Retour au menu principal")
        print()
        choix = input("  Votre choix : ").strip()

        if choix == "1":
            print("\n  -- NOUVEAU PROFESSEUR --")
            nom        = input("  Nom         : ").strip()
            prenom     = input("  Prénom      : ").strip()
            email      = input("  Email       : ").strip()
            specialite = input("  Spécialité  : ").strip()
            tel        = input("  Téléphone   : ").strip()
            if nom and prenom:
                p = ecole.ajouter_professeur(nom, prenom, email, specialite, tel)
                ecole.sauvegarder()
                print(f"\n  ✓ Professeur ajouté ! ID : {p.get_id()}")
            else:
                print("  [!] Nom et prénom obligatoires.")
            pause()

        elif choix == "2":
            profs = ecole.get_tous_professeurs()
            print(f"\n  -- LISTE DES PROFESSEURS ({len(profs)}) --")
            if not profs:
                print("  Aucun professeur enregistré.")
            else:
                print(f"  {'ID':<10} {'NOM COMPLET':<25} {'SPECIALITE'}")
                print("  " + "-"*50)
                for p in profs:
                    print(f"  {p.get_id():<10} {p.get_nom_complet():<25} "
                          f"{p.get_specialite()}")
            pause()

        elif choix == "3":
            id_p = input("\n  ID du professeur : ").strip()
            p    = ecole.get_professeur(id_p)
            if p:
                p.afficher_info()
            else:
                print("  [!] Professeur non trouvé.")
            pause()

        elif choix == "4":
            id_p = input("\n  ID du professeur : ").strip()
            p    = ecole.get_professeur(id_p)
            if p:
                code_m = input("  Code de la matière : ").strip().upper()
                m      = ecole.get_matiere(code_m)
                if m:
                    p.ajouter_matiere(m.get_nom())
                    m.set_professeur(id_p)
                    ecole.sauvegarder()
                    print(f"  ✓ Matière '{m.get_nom()}' assignée à "
                          f"{p.get_nom_complet()}.")
                else:
                    print("  [!] Matière non trouvée.")
            else:
                print("  [!] Professeur non trouvé.")
            pause()

        elif choix == "5":
            id_p    = input("\n  ID du professeur à supprimer : ").strip()
            confirm = input("  Confirmer ? (o/n) : ").strip().lower()
            if confirm == "o":
                if ecole.supprimer_professeur(id_p):
                    ecole.sauvegarder()
                    print("  ✓ Professeur supprimé.")
                else:
                    print("  [!] Professeur non trouvé.")
            pause()

        elif choix == "0":
            break


# ── Menu Matières ─────────────────────────────────────────────

def menu_matieres(ecole: Ecole):
    """Menu complet de gestion des matières."""
    while True:
        effacer_ecran()
        afficher_entete(SCHOOL_NAME)
        print("\n  === GESTION DES MATIERES ===")
        print("  1. Ajouter une matière")
        print("  2. Lister toutes les matières")
        print("  3. Supprimer une matière")
        print("  0. Retour au menu principal")
        print()
        choix = input("  Votre choix : ").strip()

        if choix == "1":
            print("\n  -- NOUVELLE MATIERE --")
            code    = input("  Code (ex: MATH101) : ").strip().upper()
            nom     = input("  Nom complet        : ").strip()
            credits = lire_entier("  Crédits            : ")
            if code and nom:
                ecole.ajouter_matiere(code, nom, credits)
                ecole.sauvegarder()
                print(f"  ✓ Matière '{nom}' ajoutée.")
            else:
                print("  [!] Code et nom obligatoires.")
            pause()

        elif choix == "2":
            matieres = ecole.get_toutes_matieres()
            print(f"\n  -- MATIERES ({len(matieres)}) --")
            if not matieres:
                print("  Aucune matière enregistrée.")
            else:
                for m in matieres:
                    m.afficher_info()
            pause()

        elif choix == "3":
            code    = input("\n  Code de la matière : ").strip().upper()
            confirm = input("  Confirmer ? (o/n) : ").strip().lower()
            if confirm == "o":
                if ecole.supprimer_matiere(code):
                    ecole.sauvegarder()
                    print("  ✓ Matière supprimée.")
                else:
                    print("  [!] Matière non trouvée.")
            pause()

        elif choix == "0":
            break


# ── Menu Notes & Absences ─────────────────────────────────────

def menu_notes_absences(ecole: Ecole):
    """Menu de gestion des notes, absences et bulletins."""
    while True:
        effacer_ecran()
        afficher_entete(SCHOOL_NAME)
        print("\n  === NOTES & ABSENCES & BULLETINS ===")
        print("  1. Ajouter une note à un étudiant")
        print("  2. Enregistrer une absence")
        print("  3. Voir le bulletin d'un étudiant")
        print("  4. Statistiques d'une classe")
        print("  0. Retour au menu principal")
        print()
        choix = input("  Votre choix : ").strip()

        if choix == "1":
            id_e   = input("\n  ID de l'étudiant   : ").strip()
            code_m = input("  Code de la matière : ").strip().upper()
            note   = lire_float("  Note (0 à 20)      : ", 0, 20)
            if ecole.ajouter_note(id_e, code_m, note):
                ecole.sauvegarder()
                print(f"  ✓ Note {note} ajoutée avec succès.")
            else:
                print("  [!] Étudiant ou matière introuvable.")
            pause()

