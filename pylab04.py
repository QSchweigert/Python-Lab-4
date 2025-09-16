import turtle
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
    t.fillcolor("green")
    t.begin_fill()
    t.left(90)
    t.forward(radius // 2)
    t.left(90)
    t.forward(radius //5)
    t.left(90)
    t.forward(radius // 2)
    t.left(90)
    t.forward(radius // 5)
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
    for _ in range(5):
        t.forward(width // 5)
        t.left(120)
        t.forward(width // 5)
        t.right(120)
    t.end_fill()



t = turtle.Turtle()
t.shape("turtle")
t.speed(10)
#t.hideturtle()

screen = turtle.Screen()
screen.bgcolor("#ff8000")

screen.setup(600, 800)

t.clear()

"""Draw Calls to Functions Here"""

#draw_square(t, 100)
#draw_circle(t, 50)
#draw_polygon(t, 5, 75)
draw_pumpkin(t, 0, -100, 100)
draw_eye(t, 40, 0, 30)
draw_eye(t, -40, 0, 30)
draw_mouth(t, -50, -50, 100)

turtle.exitonclick()