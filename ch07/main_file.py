
def main():
    data = [
        {
            "userId": 1,
            "id": 1,
            "title": "delectus aut autem",
            "completed": False
        },
        {
            "userId": 1,
            "id": 2,
            "title": "quis ut nam facilis et officia qui",
            "completed": False
        },
        {
            "userId": 1,
            "id": 3,
            "title": "fugiat veniam minus",
            "completed": False
        },
        {
            "userId": 1,
            "id": 4,
            "title": "et porro tempora",
            "completed": True
        }
    ]


    with open("todos.csv",'w') as f:
        header = data[0].keys()
        # h = "{};{};{};{}".format(*header)
        h = ";".join(header)
        
        print(h,file=f)

        for dict_value in data:
            data_line = [str(d) for d in dict_value.values()]
            line = ";".join(data_line)
            print(line,file=f)
            # print(dict_value['title'])            



def main_read_file():
    nom_fichier = "le_fichier.txt"

    # with open(nom_fichier,'r') as f:
    with open(nom_fichier) as f:
        for line in f:
            # print(line,end="")
            print(line.strip())


def main_write_file():
    nom_fichier = "le_fichier.txt"

    # ma_liste = ['Valeur 01','Valeur 02','Valeur 03','Valeur 04','Valeur 05']

    ma_liste = [f"Valeur {v:02}" for v in range(1, 15)]

    print(ma_liste)
    with open(nom_fichier, 'w') as f:
        for line in ma_liste:
            print(line, file=f)


if __name__ == '__main__':
    main()
