# 6. Használd a for ciklust, hogy egy teknőccel kirajzoltasd ezeket a szabályos sokszögeket (a szabályos azt jelenti, hogy minden oldala egyforma hosszú és minden szöge azonos):
#     • Egyenlo oldalú háromszög ˝
#     • Négyzet
#     • Hexagon (hatszög)
#     • Oktagon (nyolcszög)

import turtle
peti = turtle.Turtle()
def tekRajz(hosszusag, szog, oldalak):
    for i in range(oldalak):
        peti.forward(hosszusag)
        peti.left(szog)

tekRajz(100,120,3)
tekRajz(100,90,4)
tekRajz(100,60,6)
tekRajz(100,45,8)