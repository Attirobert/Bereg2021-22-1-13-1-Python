from született_alap import Nev
lista = []
for i in range(3):
    ember = Nev(input("Add meg a nevet! "),input("Add meg a nemét (f/n)! "), input("Add meg a foglalkozását! "))
    lista.append(ember)
x = open("születettki.txt", "w")
for i in lista:
    print(i.kiirat())
    x.write(i.kiirat())
    x.writelines("\n")
x.close()