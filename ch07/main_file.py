



def main():
    nom_fichier = "le_fichier.txt"
    
    
    # ma_liste = ['Valeur 01','Valeur 02','Valeur 03','Valeur 04','Valeur 05']
    
    ma_liste = [f"Valeur {v:02}" for v in range(1,15)]


    print(ma_liste)    
    with open(nom_fichier,'w') as f:
        for line in ma_liste:
            print(line,file=f)


if __name__ == '__main__':
    main()