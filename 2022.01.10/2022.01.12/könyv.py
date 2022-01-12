def konyv(oldalak):
    if oldalak >= 150:
        return True
    else:
        return False
cim = input("Add meg a könyv címét! ")
while cim:
    oldalak = int(input("Add meg az oldalainak számát! "))
    if konyv(oldalak):
        print(cim, "hosszú terjedelmű könyv")
    else:
        print(cim, "rövid terjedelmű könyv")
    cim = input("Add meg a könyv címét! ")