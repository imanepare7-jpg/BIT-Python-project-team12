# ── Imports ──────────────────────────────────────────────────
from ecole      import Ecole
from menus      import menu_principal
from constants  import SCHOOL_NAME
from models     import Etudiant, Professeur   


# ── Fonction principale ───────────────────────────────────────

def main():
    ecole = Ecole(SCHOOL_NAME)
    ecole.charger()          
    menu_principal(ecole) 


# ── Lancement ─────────────────────────────────────────────────
if __name__ == "__main__":
    main()
