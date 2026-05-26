#HumanBF is the class that other must heritate
class HumanBF:
    def __init__(self,ID,nom,prenom,sexe,email):
        self.id=ID
        self.Nom=nom
        self.Sexe=sexe
        self.Prenom=prenom
        self.Email=email 
    
    
    def get_id(self):
        return self.id
    
    def get_Nom(self):
        return self.Nom
    
    def get_Sexe(self):
        return self.Sexe
    
    def get_Prenom(self):
        return self.Prenom
    
    def get_Email(self):
        return self.Email
    
    #This permits to obtain the full name
    def completeName(self):
        return f"{self.Prenom} {self.Nom}"
    
    #This allows to print informations
    def Affichage(self):
        print(f"ID   :{self.id}")
        print(f"Name   :{self.completeName}")
        print(f"Sexe   :{self.Sexe}")
        print(f"Email   :{self.Email}")
