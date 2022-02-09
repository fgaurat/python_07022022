
def main():
    
    # Construire objet r à partir de la classe Rectangle
    r = Rectangle(2,3)# longueur 2 et largeur 3

    print(r.get_largeur()) # 3
    r.set_largeur(5)
    print(r.get_largeur()) # 5

if __name__ == '__main__':
    main()