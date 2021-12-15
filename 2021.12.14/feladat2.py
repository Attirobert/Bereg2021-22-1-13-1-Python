def napok_hozzaadasa2(kezdo_nap, hany_nap_mulva):
    napok = ["hétfő", "kedd", "szerda", "csütörtök", "péntek", "szombat", "vasárnap"]
    return napok[(napok.index(kezdo_nap) + hany_nap_mulva) % 7]

def honap_napja2(honap):
    honap2 = ["január", "február", "november", "december"]
    honap_napszam = [31, 28, 30, 31]
    ho = honap2.index(honap)
    return honap_napszam[ho]

def masodpercre_valtas2(ora, perc, masodperc):
    mp = ora * 3600 + perc * 60 + masodperc
    return mp

def masodpercre_valtas3(ora, perc, masodperc):
    mp = ora * 3600 + perc * 60 + masodperc
    return int(mp)