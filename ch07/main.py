


def main():
    a = 10
    b = 3
    c=a/b

    # ma_chaine = "valeur de a : {0}".format(a)
    ma_chaine = f"valeur de a : {a:02x}"
    ma_chaine_c =f"valeur de {a} / {b} = {c*100:.2f}%"
    ma_chaine_c2 =f"valeur de {a} / {b} = {c:.2%}"
    print('valeur de a '+str(a))
    print('valeur de a',a)
    print(ma_chaine)
    print(ma_chaine_c)
    print(ma_chaine_c2)
    
    # ma_chaine = f"{b=},{a=} , {c=}"
    print(ma_chaine)

    s = "Fred"

    print(f"hello {s:<10}, comment ça va ?")
    print(f"hello {s:>10}, comment ça va ?")
    print(f'{a}')
    print(f'val : {a:5d} fin')

if __name__ == '__main__':
    main()