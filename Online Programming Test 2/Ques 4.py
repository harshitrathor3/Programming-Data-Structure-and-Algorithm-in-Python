from math import sqrt
def sumofcubes(n):
    for i in range(sqrt(n)):
        for j in range(sqrt(n)):
            if i**3 + j**3 ==n:
                return True
    return False
