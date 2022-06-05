from math import sqrt
def cubefree(n):
    for i in range(2,int(sqrt(n))):
        if ((n%(i**3))==0):
            return False
    return True
