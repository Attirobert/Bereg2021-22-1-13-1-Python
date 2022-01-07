f = open("2022.01.07\osztaly.txt", "r")
xs = f.readlines()
f.close()

xs.sort()

g = open("rendezett.txt", "w")
for v in xs:
    g.write(v)
g.close()
