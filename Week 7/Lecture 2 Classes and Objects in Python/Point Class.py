from math import sqrt, atan
class Point:
    def __init__(self, a=0, b=0):
        self.r = sqrt(a*a + b*b)

        if a==0:
            self.theta = 0
        else:
            self.theta = atan(b/a)

    def Odistance(self):
        return self.r
