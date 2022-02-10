from Rectangle import Rectangle
from Carre import Carre
from Cercle import Cercle
from ICalcGeo import ICalcGeo

def show_surface(obj:ICalcGeo):
    print("show_surface",obj.surface)
    

def main():
    r = Rectangle(5,6)
    c = Carre(5)
    ce =Cercle(2)

    print(c.surface)
    c.cote = 2
    c.toto = 12
    print(c.surface)
    print(c.longueur)
    c.longueur = 12
    print("surface",ce.surface)

    show_surface(r)
    show_surface(c)
    show_surface(ce)

if __name__ == '__main__':
    main()