from unitTeszSajat import teszt
from feladatok import fordulj_orajarasi_iranyba, nap_nev,napnev
from feladatok import napok_szamitas,napszam,napok_hozzaadasa

if False:
    teszt(fordulj_orajarasi_iranyba("É") == "K")
    teszt(fordulj_orajarasi_iranyba("K") == "D")
    teszt(fordulj_orajarasi_iranyba("D") == "Ny")
    teszt(fordulj_orajarasi_iranyba("Ny") == "É")
    teszt(fordulj_orajarasi_iranyba("x") == None)

if False:
    teszt(nap_nev(0) == "Hétfő")
    teszt(nap_nev(1) == "Kedd")
    teszt(nap_nev(2) == "Szerda")
    teszt(nap_nev(3) == "Csütörtök")
    teszt(nap_nev(4) == "Péntek")
    teszt(nap_nev(5) == "Szombat")
    teszt(nap_nev(6) == "Vasárnap")
    teszt(nap_nev(7) == None)
if False:
    teszt(napnev(0) == "Hétfő")
    teszt(napnev(1) == "Kedd")
    teszt(napnev(2) == "Szerda")
    teszt(napnev(3) == "Csütörtök")
    teszt(napnev(4) == "Péntek")
    teszt(napnev(5) == "Szombat")
    teszt(napnev(6) == "Vasárnap")
    teszt(napnev(7) == None)

if False:
    teszt(napok_szamitas("Hétfő") == 0)
    teszt(napok_szamitas("Kedd") == 1)
    teszt(napok_szamitas("Szerda") == 2)
    teszt(napok_szamitas("Csütörtök") == 3)
    teszt(napok_szamitas("Péntek") == 4)
    teszt(napok_szamitas("Szombat") == 5)
    teszt(napok_szamitas("Vasárnap") == 6)
    teszt(napok_szamitas("x") == None)
if False:
    teszt(napszam("Hétfő") == 0)
    teszt(napszam("Kedd") == 1)
    teszt(napszam("Szerda") == 2)
    teszt(napszam("Csütörtök") == 3)
    teszt(napszam("Péntek") == 4)
    teszt(napszam("Szombat") == 5)
    teszt(napszam("Vasárnap") == 6)
    teszt(napszam("x") == None)

if True:
    teszt(napok_hozzaadasa("Hétfő", 4) == "Péntek")
    teszt(napok_hozzaadasa("Kedd", 0) == "Kedd")
    teszt(napok_hozzaadasa("Kedd", 14) == "Kedd")
    teszt(napok_hozzaadasa("Vasárnap", 100) == "Kedd")

