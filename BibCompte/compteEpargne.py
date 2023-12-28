from BibCompte import compte
import json

class CompteEpargne(compte.Compte):
    # Inherits from the 'compte.Compte' class

    def __init__(self, proprietaire, solde, interet):
        # Calls the constructor of the parent class
        super().__init__(proprietaire, solde)
        self.__interet = interet

    @property
    def Getinteret(self):
        return self.__interet
    
    def __str__(self):
        # Overrides the __str__ method to include interest rate information
        return super().__str__(), f"avec un taux interet {self.Getinteret}"
