from Rectangle import Rectangle
from Carre import Carre

def main():
    c = Carre(5)
    print(c.surface)
    c.cote = 2
    c.toto = 12
    print(c.surface)
    print(c.longueur)
    c.longueur = 12


if __name__ == '__main__':
    main()