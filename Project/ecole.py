

import os
import json
import datetime
from typing import Optional

from models.student import Student
from models.teacher import Teacher
from models.subject import Subject
from constants import DATA_FILE, PASSING_GRADE


class School:

    def __init__(self, name: str):

        self.__name                  = name
        self.__studends: dict       = {}   
        self.__teacher: dict     = {}   
        self.__subject: dict        = {}   
        self.__student_counter: int = 1
        self.__teacher_counter: int    = 1

    def get_name(self) -> str:

        return self.__nom

    # ── Student Management ─────────────────────────────────────

    def add_student(self, name: str, first name: str, email: str, classe: str, date_of_birth: str) -> Student:

        student_id = f"STU{self.__student_counter:04d}"
        self.__student_counter += 1    # arithmetic incrementation
        student = Student(student_id, name, first_namme, email,student_class, date_of_birth)
        self.__students[student_id] = student
        return student

    def get_student(self, student_id: str) -> Optional[Student]:

        return self.__student.get(student_id)

    def get_all_students(self) -> list:
  
        return list(self.__student.values())

    def delete_student(self, student_.id: str) -> bool:

        if student_id in self.__students:
            del self.__student[student_id]
            return True
        return False

    def search_student(self, terme: str) -> list:

        terme = terme.lower()
        return [
            e for e in self.__etudiants.values()
            if terme in e.get_nom().lower() or terme in e.get_prenom().lower()
        ]

    # ── Gestion Professeurs ───────────────────────────────────

    def ajouter_professeur(self, nom: str, prenom: str, email: str,
                           specialite: str, telephone: str) -> Professeur:

        id_prof = f"PROF{self.__compteur_prof:03d}"
        self.__compteur_prof += 1
        prof = Professeur(id_prof, nom, prenom, email, specialite, telephone)
        self.__professeurs[id_prof] = prof
        return prof

    def get_professeur(self, id: str) -> Optional[Professeur]:

        return self.__professeurs.get(id)

    def get_tous_professeurs(self) -> list:

        return list(self.__professeurs.values())

    def supprimer_professeur(self, id: str) -> bool:

        if id in self.__professeurs:
            del self.__professeurs[id]
            return True
        return False

    # ── Gestion Matières ─────────────────────────────────────

    def ajouter_matiere(self, code: str, nom: str, credits: int) -> Matiere:

        matiere = Matiere(code, nom, credits)
        self.__matieres[code] = matiere
        return matiere

    def get_matiere(self, code: str) -> Optional[Matiere]:

        return self.__matieres.get(code)

    def get_toutes_matieres(self) -> list:

        return list(self.__matieres.values())

    def supprimer_matiere(self, code: str) -> bool:

        if code in self.__matieres:
            del self.__matieres[code]
            return True
        return False

    # ── Notes & Absences ─────────────────────────────────────

    def ajouter_note(self, etudiant_id: str, matiere_code: str,
                     note: float) -> bool:

        etudiant = self.get_etudiant(etudiant_id)
        matiere  = self.get_matiere(matiere_code)
        if etudiant and matiere:
            etudiant.ajouter_note(matiere.get_nom(), note)
            return True
        return False

    def enregistrer_absence(self, etudiant_id: str, matiere_code: str,
                            date: str) -> bool:

        etudiant = self.get_etudiant(etudiant_id)
        matiere  = self.get_matiere(matiere_code)
        if etudiant and matiere:
            etudiant.ajouter_absence(date, matiere.get_nom())
            return True
        return False

    # ── Bulletins ────────────────────────────────────────────

    def generer_bulletin(self, etudiant_id: str):

        etudiant = self.get_etudiant(etudiant_id)
        if not etudiant:
            print("  [!] Étudiant non trouvé.")
            return

        date_today = datetime.date.today().strftime("%d/%m/%Y")
        print(f"\n{'#'*50}")
        print(f"  {self.__nom}")
        print(f"  BULLETIN DE NOTES")
        print(f"{'#'*50}")
        print(f"  Étudiant : {etudiant.get_nom_complet()}")
        print(f"  ID       : {etudiant.get_id()}")
        print(f"  Classe   : {etudiant.get_classe()}")
        print(f"  Date     : {date_today}")
        print(f"{'-'*50}")
        print(f"  {'MATIERE':<25} {'NOTES':<15} {'MOY':>6}")
        print(f"{'-'*50}")

        notes = etudiant.get_notes()
        if not notes:
            print("  Aucune note enregistrée.")
        else:
            for matiere, liste_notes in notes.items():
                # Opérations arithmétiques
                moy       = sum(liste_notes) / len(liste_notes)
                notes_str = ", ".join([str(n) for n in liste_notes])
                statut    = "✓" if moy >= PASSING_GRADE else "✗"
                print(f"  {matiere:<25} {notes_str:<15} {moy:>5.2f} {statut}")

        print(f"{'-'*50}")
        moy_gen = etudiant.get_moyenne_generale()
        statut  = "ADMIS" if etudiant.est_admis() else "NON ADMIS"
        mention = etudiant.get_mention()
        print(f"  MOYENNE GENERALE : {moy_gen:.2f}/20")
        print(f"  MENTION          : {mention}")
        print(f"  STATUT           : {statut}")
        print(f"  ABSENCES         : {etudiant.get_nombre_absences()} absence(s)")
        print(f"{'#'*50}\n")

    # ── Statistiques ─────────────────────────────────────────

    def statistiques_classe(self, classe: str):

        etudiants = [
            e for e in self.__etudiants.values()
            if e.get_classe() == classe
        ]
        if not etudiants:
            print(f"  [!] Aucun étudiant dans la classe {classe}.")
            return

        moyennes = [e.get_moyenne_generale() for e in etudiants]
        admis    = [e for e in etudiants if e.est_admis()]

        # Opérations arithmétiques
        moy_classe    = sum(moyennes) / len(moyennes)
        note_max      = max(moyennes)
        note_min      = min(moyennes)
        taux_reussite = (len(admis) / len(etudiants)) * 100

        print(f"\n{'='*50}")
        print(f"  STATISTIQUES — Classe {classe}")
        print(f"{'='*50}")
        print(f"  Nombre d'étudiants : {len(etudiants)}")
        print(f"  Moyenne de classe  : {moy_classe:.2f}/20")
        print(f"  Note la plus haute : {note_max:.2f}/20")
        print(f"  Note la plus basse : {note_min:.2f}/20")
        print(f"  Taux de réussite   : {len(admis)}/{len(etudiants)} "
              f"({taux_reussite:.1f}%)")
        print(f"{'='*50}\n")

    # ── Sauvegarde / Chargement ───────────────────────────────

    def sauvegarder(self):

        data = {
            "nom":                self.__nom,
            "compteur_etudiant":  self.__compteur_etudiant,
            "compteur_prof":      self.__compteur_prof,
            "etudiants":   [e.to_dict() for e in self.__etudiants.values()],
            "professeurs": [p.to_dict() for p in self.__professeurs.values()],
            "matieres":    [m.to_dict() for m in self.__matieres.values()],
        }
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def charger(self):
  
        if not os.path.exists(DATA_FILE):
            return
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.__compteur_etudiant = data.get("compteur_etudiant", 1)
        self.__compteur_prof     = data.get("compteur_prof", 1)

        for ed in data.get("etudiants", []):
            e = Etudiant.from_dict(ed)
            self.__etudiants[e.get_id()] = e

        for pd in data.get("professeurs", []):
            p = Professeur.from_dict(pd)
            self.__professeurs[p.get_id()] = p

        for md in data.get("matieres", []):
            m = Matiere.from_dict(md)
            self.__matieres[m.get_code()] = m
