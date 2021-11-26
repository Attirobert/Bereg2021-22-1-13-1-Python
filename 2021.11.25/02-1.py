# 1. Módosítsd a programot úgy, hogy mielott létrehozod az ablakot, kérje meg a felhasználót, hogy adja meg a kívánt háttérszínt! El kell tárolnod a felhasználó válaszát egy változóban és módosítani az ablak színét a felhasználó kívánsága szerint. (Segítség: találsz egy listát az engedélyezett színekrol a http://www.tcl.tk/man/tcl8.4/TkCmd/ colors.htm címen. Ez tartalmaz pár elég szokatlan színt is, mint például a „HotPink”, azaz forró rózsaszín.)

# 2. Végezz el hasonló változtatásokat, hogy a felhasználó futásidoben meg tudja adni Eszti tollának a színét!

# 3. Csináld meg ugyanezt a toll vastagsággal! Segítség: a felhasználóval folytatott párbeszéd során egy sztringet fogsz visszakapni, de Eszti pensize metódusa egész típusú értéket vár paraméterként. Szóval neked kell a sztringet int típusúvá konvertálnod, mielőtt átadnád a pensize metódusnak.
import turtle # Lehetové teszi a tekn ˝ oc használatát 
ablak = turtle.Screen() # Hozz létre egy játszóteret a teknocnek!
ablak.bgcolor("lightgreen") # Állítsd be az ablak háttérszínét!
ablak.title("Hello, Sanyi!") # Állítsd be az ablak címét!
hatterszin = input("Adja meg az ablak színét: ")
ablak.bgcolor(hatterszin)
Sanyi = turtle.Turtle() # Hozz létre egy teknocöt Sanyi néven!
Sanyi.color("blue")
szin = input("Adja meg Sanyi színét: ")
Sanyi.color(szin)
Sanyi.pensize(3)
tollvastagsag = int(input("Adja meg a toll vastagságát: "))
Sanyi.pensize(tollvastagsag)
for i in range(4):
    Sanyi.forward(100) # Sanyi menjen 50 egységet elore! 
    Sanyi.left(90) # Sanyi forduljon 90 fokot!

ablak.mainloop() # Várj, amíg a felhasználó bezárja az ablakot!
