# 7. Egy részeg kalóz véletlenszerűen fordul egyet majd megy 100 lépést, tesz még egy véletlen fordulatot és még 100 lépést, és így tovább. Egy bölcsész hallgató feljegyzi az összes fordulat szögét mielott a kalóz megtenné a következo 100 lépést. Az ő kísérletének adatai  [160, -43, 270, -97, -43, 200, -940, 17, -86]. (A pozitív szögek az óra járásával ellentétes irányúak.) Használj egy teknőcöt, hogy kirajzold részeg barátunk útvonalát!

import turtle
kaloz = turtle.Turtle()
adatok = [160, -43, 270, -97, -43, 200, -940, 17, -86]
for i in adatok:
    kaloz.left(i)
    kaloz.forward(100)
print(kaloz.heading(), "fok felé néz.")
