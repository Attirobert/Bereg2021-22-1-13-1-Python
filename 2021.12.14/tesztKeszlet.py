from unitTeszSajat import teszt
from feladat import napok_hozzaadasa, honap_napja, tenyezo_e, tobbszorose_e, celsiusra_valtas, fahrenheitre_valtas
from feladat2 import napok_hozzaadasa2, honap_napja2, masodpercre_valtas2, masodpercre_valtas3

if False:
    teszt(masodpercre_valtas2(2, 30, 10) == 9010)
    teszt(masodpercre_valtas2(2, 0, 0) == 7200)
    teszt(masodpercre_valtas2(0, 2, 0) == 120)
    teszt(masodpercre_valtas2(0, 0, 42) == 42)
    teszt(masodpercre_valtas2(0, -10, 10) == -590)

if True:
    teszt(masodpercre_valtas3(2.5, 0, 10.71) == 9010)
    teszt(masodpercre_valtas3(2.433,0,0) == 8758)

if False:
    teszt(napok_hozzaadasa2("hétfő", 4) == "péntek")
    teszt(napok_hozzaadasa2("kedd", 0) == "kedd")
    teszt(napok_hozzaadasa2("kedd", 14) == "kedd")
    teszt(napok_hozzaadasa2("vasárnap", 100) == "kedd")
    teszt(napok_hozzaadasa2("vasárnap", -1) == "szombat")
    teszt(napok_hozzaadasa2("vasárnap", -7) == "vasárnap")
    teszt(napok_hozzaadasa2("kedd", -100) == "vasárnap")

if False:
    teszt(honap_napja2("február") == 28)
    teszt(honap_napja2("november") == 30)
    teszt(honap_napja2("december") == 31)

if False:
    teszt(napok_hozzaadasa("Vasárnap", -1) == "Szombat")
    teszt(napok_hozzaadasa("Vasárnap", -7) == "Vasárnap")
    teszt(napok_hozzaadasa("Kedd", -100) == "Vasárnap")

if False:
    teszt(honap_napja("Február") == 28)
    teszt(honap_napja("November") == 30)
    teszt(honap_napja("December") == 31)

if False:
    teszt(masodpercre_valtas(2, 30, 10) == 9010)
    teszt(masodpercre_valtas(2, 0, 0) == 7200)
    teszt(masodpercre_valtas(0, 2, 0) == 120)
    teszt(masodpercre_valtas(0, 0, 42) == 42)
    teszt(masodpercre_valtas(0, -10, 10) == -590)

if False:
    teszt(tenyezo_e(3, 12))
    teszt(not tenyezo_e(5, 12))
    teszt(tenyezo_e(7, 14))
    teszt(not tenyezo_e(7, 15))
    teszt(tenyezo_e(1, 15))
    teszt(tenyezo_e(15, 15))
    teszt(not tenyezo_e(25, 15))

if False:
    teszt(tobbszorose_e(12, 3))
    teszt(tobbszorose_e(12, 4))
    teszt(not tobbszorose_e(12, 5))
    teszt(tobbszorose_e(12, 6))
    teszt(not tobbszorose_e(12, 7))
    teszt(tobbszorose_e(12, 7))

if False:
    teszt(celsiusra_valtas(212) == 100) # A víz forráspontja
    teszt(celsiusra_valtas(32) == 0) # A víz fagyáspontja
    teszt(celsiusra_valtas(-40) == -40) # Ó, micsoda érdekes eset!
    teszt(celsiusra_valtas(36) == 2)
    teszt(celsiusra_valtas(37) == 3)
    teszt(celsiusra_valtas(38) == 3)
    teszt(celsiusra_valtas(39) == 4)
if False:
    teszt(fahrenheitre_valtas(0) == 32)
    teszt(fahrenheitre_valtas(100) == 212)
    teszt(fahrenheitre_valtas(-40) == -40)
    teszt(fahrenheitre_valtas(12) == 54)
    teszt(fahrenheitre_valtas(18) == 64)
    teszt(fahrenheitre_valtas(-48) == -54)
