from szuletett_alap import Ember
import random 

lista = []
for i in range(3):
    o = Ember()
    o.setnev(input("Kérem az emberünk nevét  "))
    o.setfoglalkozas(input("add meg mit dolgozik   "))
    o.setnem(input("Add meg a nemét (f/n)"))
    lista.append(o)
for i in lista:
    print(i.getnev(), " egy ", i.getfoglalkozas()," ", i.getnem(), " volt, szerencseszáma ", random.randrange(1, 50))