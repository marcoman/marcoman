#squareSpiral.py - Draws a square spiral
import turtle
t = turtle.Pen()
colors = ["red", "orange", "green", "blue"]
for x in range(20):
    t.pencolor(colors[x%4])
    t.forward(x)
    t.left(500)
