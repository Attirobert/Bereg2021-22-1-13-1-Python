import turtle #teknős bekérése

ablak = turtle.Screen() #ablak létrehozása a teknőcnek
ablak.bgcolor("lightblue") #ablak háttérszíne
ablak.title("void négyzet") #ablak címkéje
def negyzet(x): #létrehozzuk a "négyzet" függvényt
    toll = turtle.Turtle() #létrehozzuk a tollat
    toll.color("red") #toll színét változtatjuk
    toll.pensize(4) #toll vastagságát változtatjuk
    toll.penup() #toll felemeljük
    toll.goto(x, 50) #megadjuk hogy a teknőc hol kezdjen
    toll.pendown() #letesszük a tollat
    for i in range(4): #létrehozzuk a for ciklust ami 4x fog lefutni
        toll.forward(40) #megadjuk hogy a teknőc 40 egységet menjen előre
        toll.left(90) #megadjuk hogy a teknőc 90-al elforduljon
a = -100 #létrehozzuk az "a" változót ami = -100-al, ez adja meg a kezdő helyet.        
for i in range(5): #létrehozzuk a for ciklust ami 5x fog lefutni
    negyzet(a) #végrehajtujk a negyzet fügvényt
    a += 60 #lefutás után a kezdő értéket módositom

ablak.mainloop() #ablak elején megáll.