#Creating a racing turtle game using loops and drawing a race track

from turtle import *
from random import randint

speed(10)
penup()
goto(-140,140)
for step in range(25):
  write(step, align='center')
  right(90)
  forward(10)
  pendown()
  forward(150)
  penup()
  backward(160)
  left(90)
  forward(20)
#ada
ada = Turtle()
ada.color('red')
ada.shape('turtle')

ada.penup()
ada.goto(-160, 100)
ada.pendown()
#bob
bob = Turtle()
bob.color('blue')
bob.shape('turtle')

bob.penup()
bob.goto(-160, 70)
bob.pendown()
#leo
leo = Turtle()
leo.color('green')
leo.shape('turtle')

leo.penup()
leo.goto(-160, 40)
leo.pendown()

#dona
dona = Turtle()
dona.color('yellow')
dona.shape('turtle')

dona.penup()
dona.goto(-160, 10)
dona.pendown()


for turn in range(170):
  ada.forward(randint(1,5))
  bob.forward(randint(1,5))
  leo.forward(randint(1,5))
  dona.forward(randint(1,5))


