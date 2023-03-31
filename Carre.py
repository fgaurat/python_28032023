from Rectangle import Rectangle

class Carre(Rectangle):

    def __init__(self, cote):
        super().__init__(cote, cote)
        self._cote = cote
    
    @property
    def cote(self):
        return self._cote

    @cote.setter
    def cote(self,value):
        self._cote = value
        self._longueur= value
        self._largeur= value
        # self._largeur = value

    def __str__(self):
        return f"{__class__.__name__} : {self._cote=}"
