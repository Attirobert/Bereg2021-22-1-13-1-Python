class Pont:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

class Egyenes:

    def __init__(self, p1, p2):
        self.p1 = p1        
        self.p2 = p2 

    def Hossz(self):
        return (abs(self.p1.x - self.p2.x)**2 + abs(self.p1.y - self.p2.y)**2)**0.5    

    def Meredekseg(self):
        if (self.p1.x < self.p2.x): return (self.p2.x - self.p1.x) / (self.p2.y - self.p1.y)
        return (self.p1.x - self.p2.x) / (self.p1.y - self.p2.y)