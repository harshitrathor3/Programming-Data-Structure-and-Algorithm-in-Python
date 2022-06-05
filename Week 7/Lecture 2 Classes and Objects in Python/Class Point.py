from math import sqrt
class Point:
    def __init__(self, a, b):
        self.x = a
        self.y = b

    def translate(self, delx, dely):
        self.x+=delx
        self.y+=dely

    def Odistance(self):
        return sqrt(self.x*self.x+self.y*self.y)
