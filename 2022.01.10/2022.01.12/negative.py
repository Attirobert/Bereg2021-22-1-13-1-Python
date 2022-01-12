szam1 = int(input("Adj meg egy számot! "))
szam2 = int(input("Add meg a második számot! "))

if szam1 > 0 and szam2 > 0:
    print("A két szám közül egyik sem negatív")
elif szam1 > 0 and szam2 < 0:
    print("A két szám közül a második negatív")
elif szam1 < 0 and szam2 > 0:
    print("A két szám közül az első negatív")
else:
    print("A mind a két szám negatív")


