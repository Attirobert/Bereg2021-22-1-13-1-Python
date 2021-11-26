# 7. Írj egy Python programot az előző feladat általános megoldására. Kérd be a felhasználótól az aktuális időt (csak az órákat) és azt, hogy hány órával késobb szólaljon meg az ébresztőóra, majd jelenítsd meg a képernyőn, hogy hány órakor fog megszólalni az ébresztőóra. 
most = int(input("Aktuális idő:"))
eltelt = int(input("Pihenő idő:"))
maradek = (most+eltelt)%24
napok = (most+eltelt)//24
print("Ébresztés időpontja: ",str(napok)+". nap",maradek,"óra")
