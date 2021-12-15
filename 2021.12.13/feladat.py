from unitTeszSajat import teszt

def abszolut_ertek(p):
    """ Abszolút érték meghatározása"""

    if (p >= 0): return p
    else: return -p

# Tesztkészlet megadása
teszt(abszolut_ertek(0) == 0)
teszt(abszolut_ertek(-1) == 1)
teszt(abszolut_ertek(1) == 1)
teszt(abszolut_ertek(10) == 10)
teszt(abszolut_ertek(-10) == 10)