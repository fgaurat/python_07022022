from ICalcGeo import ICalcGeo


class Rectangle(ICalcGeo):

    _cpt=0

    # Constructeur
    def __init__(self,longueur=0,largeur=0) -> None:
        print(f"def __init__(self,{longueur},{largeur})")
        self._longueur = longueur
        self._largeur = largeur
        Rectangle._cpt+=1
    
    
    @property
    def longueur(self):
        return self._longueur

    @property
    def largeur(self):
        return self._largeur

    @longueur.setter
    def longueur(self,longueur):
        self._longueur = longueur
    
    @largeur.setter
    def largeur(self,largeur):
        self._largeur = largeur

    @property
    def surface(self):
        return self._longueur*self._largeur

    def __str__(self) -> str:
        to_string = f'Rectangle longueur : {self._longueur},largeur : {self._largeur}'
        return to_string
    
    def get_cpt():
        return Rectangle._cpt

    def __del__(self):
        print("def __del__(self)")
        Rectangle._cpt-=1