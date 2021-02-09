#Рисуем

import turtle
w=turtle.getscreen()
w.bgcolor("pink")
ds=turtle.Turtle()
ds.shape("turtle")
ds.color("green")
distance=100
ds.up()
for i in  range(12):
    ds.forward(distance)
    ds.right(90)
    ds.stamp()
    distance=distance+10

ds.goto(-250,100)
ds.color("blue")
ds.down()
for i in range(72):
    ds.forward(5)
    ds.right(5)

ds.up()
ds.goto(0,-300)
distance=10
for i in range(10):
    ds.forward(distance)
    ds.stamp()
    distance=distance+20



w.exitonclick ()



