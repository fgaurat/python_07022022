
import traceback
def main():
    try:
        a = 2
        b = 0
        c = a/b
        print("c",c)
    

    except Exception as e:
        traceback.print_exc()
        print("Exception erreur",e)

if __name__ == '__main__':
    main()
