


class Rectangle:


    def __init__(self,longueur=0,largeur=0) -> None:
        print(f"def __init__(self,{longueur},{largeur})")
        self._longueur = longueur
        self._largeur = largeur
    
    def get_longueur(self):
        return self._longueur

    def get_largeur(self):
        return self._largeur
