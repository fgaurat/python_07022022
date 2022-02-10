from Rectangle import Rectangle

def main():
    
    # Construire objet r à partir de la classe Rectangle
    r = Rectangle(2,3)# longueur 2 et largeur 3
    print(f"nombre d'objet : {Rectangle.get_cpt()}")
    r1 = Rectangle()# longueur 2 et largeur 3
    print(f"nombre d'objet : {Rectangle.get_cpt()}")
    
    
    print(r.largeur) # 3
    print(r.longueur) # 2
    r.largeur = 5
    print(r.largeur) # 5

    print(type(r))

    print("surface",r.surface)
    # r.set_surface(12)
    # r.surface = 12 => pas possible


    del r1

    the_chaine = str(r)
    print(the_chaine)

    print("fin")

if __name__ == '__main__':
    main()