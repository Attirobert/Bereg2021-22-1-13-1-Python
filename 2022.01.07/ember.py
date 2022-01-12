class Ember:
    def __init__(self, p1 = "Anonimus", p2 = "zöld", p3 = "barna"):
        self.nev = p1
        self.szem = p2
        self.haj = p3

    def setHaj(self, haj):
        self.haj = haj

    def getHaj(self):
        return self.haj

    def setNev(self, nev):
        self.nev = nev

    def getNev(self):
        return self.nev

    def koszon(self):
        print("Szia! A nevem: {0}".format(self.nev))


# Megteremtjük Ádámot
adam = Ember()
print("Ádám neve: ", adam.getNev())
adam.setNev("Ádám")
print("Ádám neve: ", adam.getNev())
print(adam.koszon())

# Megteremtjük Évát
eva = Ember("Éva", "Kék", "Szőke")
print("Éva neve: ", eva.getNev())
print("Éva haja: ", eva.getHaj())
print(eva.koszon())

