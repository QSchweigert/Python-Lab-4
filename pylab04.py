import turtle
import random
"""Functions Here"""

#def draw_square(t, length):
  #  for _ in range(4):
       # t.forward(length)
       # t.left(90)

#def draw_circle(t, radius):
   # t.circle(radius)

def draw_polygon(t, sides, length):
    angle = 360 / sides
    for _ in range(sides):
        t.forward(length)
        t.left(angle)

def draw_pumpkin(t, x, y, radius):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("orange")
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

    #stem
    base = radius // 5
    side = radius // 2
    t.penup()
    t.goto(x + base //2, y + 2*0.99*radius)
    t.pendown()
    t.fillcolor("green")
    t.begin_fill()
    t.left(90)
    t.forward(side)
    t.left(90)
    t.forward(base)
    t.left(90)
    t.forward(side)
    t.left(90)
    t.forward(base)
    t.end_fill()

def draw_eye(t, x, y, size):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    draw_polygon(t, 3, size)
    t.end_fill()

def draw_mouth(t, x, y, width):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    t.right(60)
    for _ in range(5):
        t.forward(width // 5)
        t.left(120)
        t.forward(width // 5)
        t.right(120)
    t.end_fill()
    t.left(60)

def draw_star(t, x, y, size):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("white")
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()

def draw_sky(t, num_stars):
    for _ in range(num_stars):
        x = random.randint(-300, 300)
        y = random.randint(0, 300)
        size = random.randint(10, 30)
        draw_star(t, x, y, size)

def draw_jackolantern(t, x, y, r):
    draw_pumpkin(t, x, y, r)
    s = .25*r
    draw_eye(t, x - r // 2 - s // 2, y + (2 + r) - 1.75, s)
    draw_eye(t, x + r // 2 - s, y + (2 + r) - 1.75, s)
    draw_mouth(t, x - r // 2, y + r //2, r)

t = turtle.Turtle()
t.shape("turtle")
t.speed(0)
t.hideturtle()

screen = turtle.Screen()
screen.bgcolor("purple")

screen.setup(600, 800)

t.clear()

"""Draw Calls to Functions Here"""

#draw_square(t, 100)
#draw_circle(t, 50)
#draw_polygon(t, 5, 75)
x = -200
y = -250
r = 100

#draw_pumpkin(t, x, y, r)
#draw_eye(t, x - r//2- s //2, y + (2 + r) - 1.75, s)
#draw_eye(t, x + r//2 - s, y + ( 2 + r) - 1.75, s)
#draw_mouth(t, x - r//3.5 - s, y + (2 + r) - 50, 100)
draw_jackolantern(t, x, y, r)
draw_jackolantern(t, x + 400, y, 50)
draw_jackolantern(t, x + 225, y, 75)
draw_star(t, -100, 150, 30)
draw_star(t, 100, 100, 20)
draw_sky(t, 50)
turtle.exitonclick()