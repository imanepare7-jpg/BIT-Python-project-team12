class Person:
    def __init__(self, id: str, last_name: str, first_name: str, email: str):
        self.__id         = id           
        self.__last_name  = last_name
        self.__first_name = first_name
        self.__email      = email
        
 # ── Getters (encapsulation) ──────────────────────────────

    def get_id(self) -> str:
      
        return self.__id

    def get_last_name(self) -> str:
      
        return self.__last_name

    def get_first_name(self) -> str:
       
        return self.__first_name

    def get_email(self) -> str:
        
        return self.__email

    def get_full_name(self) -> str:
       
        return f"{self.__first_name} {self.__last_name}"

    # ── Methods ──────────────────────────────────────────────

    def display_info(self)
        print(f"  ID         : {self.__id}")
        print(f"  Name       : {self.get_full_name()}")
        print(f"  Email      : {self.__email}")

    def to_dict(self) -> dict:
        """Converts the object to a dictionary for JSON saving."""
        return {
            "id":         self.__id,
            "last_name":  self.__last_name,
            "first_name": self.__first_name,
            "email":      self.__email
        }
