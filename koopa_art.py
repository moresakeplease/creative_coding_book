import turtle
from PIL import Image

t = turtle.Turtle()

colors = ['snow', 'snow1', 'snow2']
colors2 = ['seashell','seashell1', 'seashell2']
turtle.bgcolor('black')

t.hideturtle()

for n in range(72):
    for i in range(3):
        t.color(colors[i])
        t.forward(45)
        t.left(90)
        t.forward(45)
        t.right(90)
        t.forward(45) 
    t.penup()
    t.goto(0,0)
    t.pendown()
    t.right(5)

t.goto(0,0)

for n in range(72):
    for i in range(3):
        t.color(colors2[i])
        t.backward(45)
        t.right(90)
        t.backward(45)
        t.left(90)
        t.backward(45) 
    t.penup()
    t.goto(0,0)
    t.pendown()
    t.left(5)

canvas = turtle.getcanvas()
canvas.postscript(file="drawing.eps")

img = Image.open("drawing.eps")
img.save("drawing.png")

turtle.done()
    