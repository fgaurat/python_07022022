from Rectangle import Rectangle

def main():
    
    # Construire objet r à partir de la classe Rectangle
    r = Rectangle(2,3)# longueur 2 et largeur 3
    print(f"nombre d'objet : {Rectangle.get_cpt()}")
    r1 = Rectangle()# longueur 2 et largeur 3
    print(f"nombre d'objet : {Rectangle.get_cpt()}")
    
    print(r.get_largeur()) # 3
    print(r.get_longueur()) # 2
    r.set_largeur(5)
    print(r.get_largeur()) # 5

    print(type(r))

    r.get_surface()


    del r1

    the_chaine = str(r)
    print(the_chaine)

    print("fin")

if __name__ == '__main__':
    main()