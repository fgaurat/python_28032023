

from dataclasses import dataclass

@dataclass
class RectangleData:

    longueur:int = 0
    largeur:int = 0

    def surface(self):
        return self.longueur*self.largeur
