import traceback
from TwelveDivisionError import TwelveDivisionError
# import mesErreurs

def division(val_a,val_b):
    if val_b == 12:
        raise TwelveDivisionError()
        # raise mesErreurs.TwelveDivisionError()
        # e = Exception("Division par 12 !")
        # raise e
        # raise Exception("Division par 12 !")
    result = val_a/val_b
    return result

def call_division(v1,v2):
    r=0
    try:
        r = division(v1,v2)
    finally:
        print("fin call_division")
    return r



def main():
    try:
        a = 2
        b = int(input("Entrez la valeur de b:"))
        # c = a/b
        # c = division(a,b)
        c = call_division(a,b)
        print("c",c)
    
    except TwelveDivisionError as e:
    # except mesErreurs.TwelveDivisionError as e:
        print(e)
    except ZeroDivisionError as e:
        print("ZeroDivisionError",e)
        # traceback.print_exc()
    except ValueError as e:
        print("ValueError",e)
    except TypeError as e:
        print("TypeError",e)
    except Exception as e:
        # traceback.print_exc()
        print("Exception erreur",e)
    else:
        print("else c",c)
    finally:
        print("finally")



    print("fin")

if __name__ == '__main__':
    main()
