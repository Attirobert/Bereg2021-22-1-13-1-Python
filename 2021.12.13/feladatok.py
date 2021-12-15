#1. Az égtájak rövid néven: "É", "K", "Ny", "D". 
# Írjunk függvényt "fordulj_orajarasi_iranyba()"" névvel, 
# ami a paraméterként megadott égtáj után következik. 
# Rossz paraméter esetén None értéket ad vissza
def fordulj_orajarasi_iranyba(p):
    if (p == "É"): return "K"
    elif (p == "K"): return "D"
    elif (p == "D"): return "Ny"
    elif (p == "Ny"): return "É"
    return None

# 2. Írj egy nap_nev függvényt, amely a [0, 6] tartományba eso egész számot vár paraméterként, és visszaadja az adott sorszámú nap nevét. A 0. nap a hétfo. Ha nem várt érték érkezik, akkor None értékkel térj vissza.
def nap_nev(k):
    if (k == 0): return "Hétfő"
    elif (k == 1): return "Kedd"
    elif (k == 2): return "Szerda"
    elif (k == 3): return "Csütörtök"
    elif (k == 4): return "Péntek"
    elif (k == 5): return "Szombat"
    elif (k == 6): return "Vasárnap"
    return None
def napnev(t):
    napok=["Hétfő","Kedd","Szerda","Csütörtök","Péntek","Szombat","Vasárnap"]
    if t> 6:
        return None
    return napok[t]
    
#3. Írd meg az eloz˝ o függvény fordítottját, amely egy nap neve alapján adja meg annak sorszámát:
def napok_szamitas(k):
    if (k == "Hétfő"): return 0
    elif (k == "Kedd"): return 1
    elif (k == "Szerda"): return 2
    elif (k == "Csütörtök"): return 3
    elif (k == "Péntek"): return 4
    elif (k == "Szombat"): return 5
    elif (k == "Vasárnap"): return 6
    return None


def napszam(n):
    napok=["Hétfő","Kedd","Szerda","Csütörtök","Péntek","Szombat","Vasárnap"]
    if n in napok:
        return napok.index(n)
    else:
        return None

def napok_hozzaadasa(nap, napokszama):
    napok=["Hétfő","Kedd","Szerda","Csütörtök","Péntek","Szombat","Vasárnap"]
    indnap = napok.index(nap)
    vegnapszama = (indnap + napokszama) % 7
    return napok[vegnapszama]



