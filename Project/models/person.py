class Person:
    def __init__(self, id, last_name, first_name, email):
        self.id = id           
        self.last_name = last_name
        self.first_name = first_name
        self.email = email

    def get_id(self) -> str:
      
        return self._id

    def get_last_name(self) -> str:
      
        return self.last_name

    def get_first_name(self) -> str:
       
        return self.first_name

    def get_email(self) -> str:
        
        return self.email

    def get_full_name(self) -> str:
       
        return f"{self.first_name} {self.last_name}"


    def display_info(self):
        print(f"  ID         : {self.id}")
        print(f"  Name       : {self.get_full_name()}")
        print(f"  Email      : {self.email}")

    def to_dict(self) -> dict:
        """Converts the object to a dictionary for JSON saving."""
        return {
            "id": self.id,
            "last_name": self.last_name,
            "first_name": self.first_name,
            "email": self.email
        }
