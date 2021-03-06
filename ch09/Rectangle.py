


class Rectangle:

    _cpt=0

    # Constructeur
    def __init__(self,longueur=0,largeur=0) -> None:
        print(f"def __init__(self,{longueur},{largeur})")
        self._longueur = longueur
        self._largeur = largeur
        Rectangle._cpt+=1
    
    def get_longueur(self):
        return self._longueur

    def get_largeur(self):
        return self._largeur

    def set_longueur(self,longueur):
        self._longueur = longueur
    
    def set_largeur(self,largeur):
        self._largeur = largeur

    def get_surface(self):
        return self._longueur*self._largeur

    def __str__(self) -> str:
        to_string = f'Rectangle longueur : {self._longueur},largeur : {self._largeur}'
        return to_string
    
    def get_cpt():
        return Rectangle._cpt

    def __del__(self):
        print("def __del__(self)")
        Rectangle._cpt-=1