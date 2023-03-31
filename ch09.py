from Rectangle import Rectangle
from Carre import Carre
from RectangleData import RectangleData

def main():
    r = Rectangle(2,3)
    r1 = Rectangle(22,33)
    r2 = Rectangle(24,53)
    print("get_cpt()",Rectangle.get_cpt())

    print(50*'-')
    
    # print(r.get_longueur()) # 2
    print(r.longueur) # 2
    
    # assert r.get_longueur()==2

    print(r.largeur) # 3
    print(r.get_surface()) # 6

    # print('destruct')
    # del r
    # print('after destruct')

    r.largeur = 4
    print(r.get_surface()) # 8
    print(r)

    r3 = Rectangle(2,3)
    r4 = Rectangle(2,3)

    # if r3.__eq__(r4):
    if r3==r4:
        print("ok")
    else:
        print('ko')

    r3.longueur =  12
    print(r3.longueur)


    r5 = RectangleData(3,4)
    r6 = RectangleData(3,4)
    print(r5.largeur)
    print(r5.longueur)
    print(r5)

    if r5==r6:
        print("ok")
    else:
        print("ko")
    
    print(50*'-')
    c = Carre(2)
    print(c.get_surface())
    c.cote=10
    print(c.cote)
    print(c.get_surface())
    print(c)

if __name__=='__main__':
    main()
