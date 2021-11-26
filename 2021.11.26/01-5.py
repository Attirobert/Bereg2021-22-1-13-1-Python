# 5.
# Írj programot, amely meghatározza, mennyi lesz egy betét értéke a futamido végén, ha 10000 Ft-t helyezünk betétbe 8%-os névleges kamatláb mellett. Az évközi kamatozások száma (m) 12. Az évek számát, vagyis a t értékét a felhasználótól kérje be a program. A futamido végén nézett értéket (FV) az alábbi képlet alapján számold:
# FV = C * (1 + r/m)**(m*t)
# ahol:
#     c: alaptőke
#     r: éves névleges kamatláb
#     m: évközi kamatozások száma
#     t: évek száma
c = 10000
r = 0.08
m = 12
t = int(input("évek száma:"))
FV = c * (1+ r/m)**(m*t)
print("A betét értéke futamidő végén",FV)
