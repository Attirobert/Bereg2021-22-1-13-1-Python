def napok_hozzaadasa(nap, napokszama):
    napok=["Hétfő","Kedd","Szerda","Csütörtök","Péntek","Szombat","Vasárnap"]
    indnap = napok.index(nap)
    maradeknap = (napokszama % -7)
    valtozo = indnap + maradeknap 
    return napok[valtozo]
#Írj egy honap_napja függvényt, mely egy hónap
#neve alapján megadja, hogy hány nap van a hónapban.
#(A szökőévekkel ne foglalkozz.)
def honap_napja(honap):
    napok=(["Január",31],["Február",28],["Március",31],["Április",30],["Május",31],
    ["Június",30],["Július",31],["Augusztus",31],
    ["Szeptember",30],["Október",31],["November",30],["December",31])
    for i,h in (napok):
        if i == honap:
            return h 
    return None

#masodpercre_valtas függvényt, mely órákat,
#perceket és másodperceket kap meg argumentumaként,
#és kiszámolja hány másodpercnek felelnek meg összesen.


"""16. Készíts egy tenyezo_e(t, n) fejlécű függvényt, amely átmegy az alábbi teszteken. 
(Ne csak a prímtényezőkre adjon vissza igazat a függvényed"""

def tenyezo_e(t, n):
    if n % t == 0:
        return True
    return False

# 17. Írj egy tobbszorose_e fejlécű függvényt, mely kielégíti az alábbi egységtesztet

def tobbszorose_e(t, n):
    return tenyezo_e(n, t)

#rj egy celsiusra_valtas(f) függvényt, mely egy Fahrenheitben megadott értéket Celsius fokra vált át.
#A függvény a legközelebbi egész értéket adja vissza. (Segítség: Ha a beépített round függvényt szeretnéd
#használni, próbáld kiíratni a round.__doc__ -et a Python konzolban, vagy a függvény nevén állva nyomd le
#a Ctrl+Q billentyű kombinációt. Kísérletezz, ameddig rá nem jössz, hogyan működik. ):
def celsiusra_valtas(f):
    return round(5 / 9 * (f - 32))

def fahrenheitre_valtas(c):
    return round(c * 1.8 + 32)
