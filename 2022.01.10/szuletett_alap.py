class Ember:
    def __init__(self):
        self.nev = ""
        self.foglalkozas = ""
        self.nem = ""
    def setnev(self, nev):
        self.nev = nev
    def getnev(self):
        return self.nev
    def setfoglalkozas(self, foglalkozas):
        self.foglalkozas = foglalkozas
    def getfoglalkozas(self):
        return self.foglalkozas
    def setnem(self, nem):
        if nem == "f":
            self.nem = "Férfi"
        elif nem == "n":
            self.nem = "Nő"
        else:
            print("nincs ilyen nem")
    def getnem(self):
        return self.nem