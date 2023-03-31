import traceback

class DivBy12Error(Exception):


    def __init__(self):
        super().__init__("Hooooo erreur division par 12 !!!")

def div(a,b):
    if b ==12:
        # raise Exception("Hoooo Division par 12 !!!")
        raise DivBy12Error()
    return a/b

def call_div(a,b):
    try:
        print('ouverture log')
        c = div(a,b)
    finally:
        print('fermeture log')
    return c

def main():
    try:
        a =2
        b=12
        c = call_div(a,b)
        print("c",c)
        
    except ZeroDivisionError as e:
        print(e)
    except TypeError as e:
        print(e)
    except DivBy12Error as e:
        print("DivBy12Error",e)
    except Exception as e:
        print("Exception",e)
    else:
        print("pas d'erreur")
    finally:
        print("finally après")
if __name__=='__main__':
    main()
