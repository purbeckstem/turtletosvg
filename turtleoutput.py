import turtle
import Tkinter
import canvasvg
from random import randint 
from sys import exit
T = turtle.Turtle()
myWin = turtle.Screen()

def saveImg():
	T.hideturtle()
	name = raw_input("What would you like to name it? ")
	nameSav = name + ".svg"
	ts = T.getscreen().getcanvas()
	canvasvg.saveall(nameSav, ts)
#	canvasvg.saveall("image.svg", T._canvas)

T.pendown()
T.speed(0)
for i in range(1000):
        T.forward(randint(0,90))
        T.left((randint(1,3))*60)
#T.hideturtle()

#canvasvg.saveall("blah.svg", ts)


saveImg()
#T.done()
exit()
