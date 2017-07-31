import turtle


speed = 2.5

UP = 0
LEFT = 1
DOWN = 3
RIGHT = 4

direction = UP

turtle.pensize(10)
turtle.left(90)
turtle.shape("square")
turtle.penup()


UP_ARROW = "Up"
LEFT_ARROW = "Left"
DOWN_ARROW = "Down"
RIGHT_ARROW = "Right"
SPACEBAR = "space"


def up():
    direction = UP
    print(direction)

    oldPos = turtle.pos()
    x, y = oldPos
    
    turtle.goto(x, y + speed)
    print(turtle.pos())

def down():
    direction = DOWN
    print(direction)

    oldPos = turtle.pos()
    x, y = oldPos

    turtle.goto(x, y - speed)
    print(turtle.pos())

def right():
    direction = RIGHT
    print(direction)

    oldPos = turtle.pos()
    x, y = oldPos

    turtle.goto(x + speed, y)
    print(turtle.pos())

    turtle.right(90)

def left():
    direction = LEFT
    print(direction)
    

    oldPos = turtle.pos()
    x, y = oldPos

    turtle.goto(x - speed, y)
    print(turtle.pos())

    turtle.left(90)

turtle.onkeypress(up, UP_ARROW)
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)
turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(turtle.stamp, SPACEBAR)
turtle.listen()

while True:
    turtle.forward(speed)


turtle.mainloop()
