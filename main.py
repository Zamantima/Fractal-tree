import turtle
from random import randint

turtle.colormode(255)
def random_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    color_tuple = (r,g,b)
    return color_tuple

tree = turtle.Turtle()

tree.shape("arrow")
tree.speed("fastest")
def set_position():
    tree.penup()
    tree.setheading(270)
    tree.forward(250)
    tree.setheading(90)

set_position()
tree.pendown()
tree.color("brown")
tree.width(10)
def branch(length):
    if length< 10:
        return
    else:
        if length < 75:
            tree.color(random_color())
        tree.forward(length)
        tree.left(30)
        branch(3*length/4)
        tree.width(5)
        tree.right(60)
        branch(3*length/4)
        tree.left(30)
        tree.backward(length)

branch(100)
turtle.done()


Screen = turtle.Screen()
Screen.exitonclick()