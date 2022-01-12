import random
class Nev:
    def __init__(self, name, gender, work):
        self.name = name
        self.gender = gender
        self.work = work
        self.rdme = random.randint(1,50)
    def nem(self):
        if self.gender == "f":
            return "férfi"
        elif self.gender == "n":
            return "nő"
    def kiirat(self):
        return "{neve} egy {munka} {nem} volt, szerencse száma a {rdm}".format(neve=self.name,munka=self.work,nem=self.nem(),rdm=self.rdme)

