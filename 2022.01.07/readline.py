uj_kezelo = open("elso.txt", "r") # Nyisd meg a fájlt
while True:
    sor = uj_kezelo.readline() # Próbáld beolvasni a következo sort ˝
    if len(sor) == 0: # Ha nincs több sor
        break # Hagyd el a ciklust
    # Most dolgozd fel az éppen aktuálisan beolvasott sort
    print(sor, end="")

uj_kezelo.close() # Zárd be a fájlt