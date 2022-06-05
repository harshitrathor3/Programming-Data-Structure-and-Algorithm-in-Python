class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self,n):                #can only be used when just below one would commented. Reason IDK
        return 'Helo World'

    def __str__(self):
        return '('+str(self.x)+', '+str(self.y)+')'

    def __add__(self, p):
        return point(self.x+p.x, self.y+p.y)
    
