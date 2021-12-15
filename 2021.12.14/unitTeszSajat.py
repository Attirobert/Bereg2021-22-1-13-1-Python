import sys

def teszt(tesztEset):
    sorszam = sys._getframe(1).f_lineno # visszaadja a hívó sorának számát
    if tesztEset:
        msg = "A(z) {0}. sorban álló teszt sikeres".format(sorszam)
    else:
        msg = "A(z) {0}. sorban álló teszt SIKERTELEN".format(sorszam)

    print(msg)
