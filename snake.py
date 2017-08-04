import turtle
import random

turtle.tracer(1, 0)

BORDER_SIZE_X = 400
BORDER_SIZE_Y = 200
REAL_SIZE_X = 850
REAL_SIZE_Y = 550

turtle.setup(REAL_SIZE_X, REAL_SIZE_Y)
turtle.bgcolor("black")

turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 1
SCORE = 0

UP_EDGE = (BORDER_SIZE_Y)
DOWN_EDGE = -(BORDER_SIZE_Y)
RIGHT_EDGE = (BORDER_SIZE_X)
LEFT_EDGE = -(BORDER_SIZE_X)

isGrow = False

SPEED = 50

## Initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []
color_list = ["red", "lightblue", "yellow", "orange", "green", "pink", "brown", "grey", "blue", "purple"]
# Set u positions (x, y) of boxes that make up the snake
snake = turtle.clone()
snake.shape("square")
snake.fillcolor("red")

#Hide the turtle object (it's an arrow we don't need to see it)
turtle.hideturtle()


## Draw a snake at the start of the game with a for loop
## for loop should use range() and coount up to the number of pieces
## in the snake (i.e. START_LENGTH)

for i in range(START_LENGTH):
    x_pos = snake.pos()[0]
    y_pos = snake.pos()[1]

    ## Add SQUARE_SIZE to x_pos. Where does x_pos point to now?
    ## You're RIGHT!
    x_pos += SQUARE_SIZE
    my_pos = (x_pos, y_pos)
    
    snake.goto(x_pos, y_pos)

    ## Append the new position tuple to pos_list
    pos_list.append(my_pos)

    ## Save the stamp ID! You'll need to erase it later.
    ## Then append it to stamp_list
    stamp = snake.stamp()
    stamp_list.append(stamp)
    

UP_ARROW = "Up" #Make sure you pay attention to upper and lower case
LEFT_ARROW = "Left" #Pay attention to upper and lower case
DOWN_ARROW = "Down" #Pay attention to upper and lower case
RIGHT_ARROW = "Right" #Pay attention to upper and lower case
TIME_STEP = 100 #Update snake position after this many milliseconds
SPACEBAR = "space" # Careful, it's not supposed to be capitalized!
UP = 0

#1. Make variables LEFT, DOWN, and RIGHT with values 1, 2, and 3
####WRITE YOUR CODE HERE!!

DOWN = 1
LEFT = 2
RIGHT = 3


direction = UP

def up():
    global direction #snake direction is global (same everywhere)
    if direction != DOWN:
        direction = UP #Change direction to 
        
def down():
    global direction #snake direction is global (same everywhere)
    if direction != UP:
        direction = DOWN #Change direction to up

def left():
    global direction #snake direction is global (same everywhere)
    if direction != RIGHT:
        direction = LEFT #Change direction to up

def right():
    global direction #snake direction is global (same everywhere)
    if direction != LEFT:
        direction = RIGHT #Change direction to up


#2. Make functions down(), left(), and right() that change direction
####WRITE YOUR CODE HERE!!
turtle.onkeypress(up, UP_ARROW)
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)# Create listener for up key
turtle.listen()

turtle.register_shape("trash.gif")
food = turtle.clone()
food.shape("trash.gif")
turtle.hideturtle()

def createBorder():
    border = turtle.clone()
    border.pensize(10)
    turtle.colormode(255)
    border.color(221, 54, 67)
    border.goto(BORDER_SIZE_X, BORDER_SIZE_Y)

    border.pendown()
    
    border.goto(BORDER_SIZE_X, -BORDER_SIZE_Y)
    border.goto(-BORDER_SIZE_X, -BORDER_SIZE_Y)
    border.goto(-BORDER_SIZE_X, BORDER_SIZE_Y)
    border.goto(BORDER_SIZE_X, BORDER_SIZE_Y)

    
    border.penup()
    
def make_food():
    global food_stamps, food_pos, food
    #The screen positions go from -SIZE/2 to +SIZE/2
    #But we need to make food pieces only appear on game squares
    #So we cut up the game board into multiples of SQUARE_SIZE.

    min_x=-int(BORDER_SIZE_X/SQUARE_SIZE)+1
    max_x=int(BORDER_SIZE_X/SQUARE_SIZE)-1
    min_y=-int(BORDER_SIZE_Y/SQUARE_SIZE)+1
    max_y=int(BORDER_SIZE_Y/SQUARE_SIZE)-1
    #Pick a position that is a random multiple of SQUARE_SIZE
    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE
    foodPos = (food_x, food_y)
    if foodPos in pos_list:
        print("Food on body, No!")
        make_food()
    else:
        ##1.WRITE YOUR CODE HERE: Make the food turtle go to the randomly-generated
        ## position
        food.goto(food_x, food_y)
        ##2.WRITE YOUR CODE HERE: Add the food turtle's position to the food positions list
        food_pos.append(food.pos())
        ##3.WRITE YOUR CODE HERE: Add the food turtle's stamp to the food stamps list
        foodStamp = food.stamp()
        food_stamps.append(foodStamp)
    
def move_snake():
    global food_stamps, food_pos, isGrow, SCORE
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    
    if direction == RIGHT:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)

    elif direction == LEFT:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)

    elif direction == DOWN:
        snake.goto(x_pos, y_pos - SQUARE_SIZE)

    elif direction == UP:
        snake.goto(x_pos, y_pos + SQUARE_SIZE)

    #Stamp new element and append new stamp in list
    #Remember: The snake position changed - update my_pos()
    my_pos = snake.pos()
    pos_list.append(my_pos)

    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)
    ######## SPECIAL PLACE - Remember it for Part 5
    #pop zeroth element in pos_list to get rid of last the last
    if isGrow == False:
        #piece of the tail
        old_stamp = stamp_list.pop(0)
        snake.clearstamp(old_stamp)
        pos_list.pop(0)
    else:
        isGrow = False

    #Add new lines to the end of the function
    #Grab position of snake
    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]

    if new_x_pos >= RIGHT_EDGE:
        quit()

    elif new_x_pos <= LEFT_EDGE:
        quit()

    elif new_y_pos >= UP_EDGE:
        quit()

    elif new_y_pos <= DOWN_EDGE:
        quit()


    if snake.pos() in food_pos:
        food_ind = food_pos.index(snake.pos())
        food.clearstamp(food_stamps[food_ind])

        food_pos.pop(food_ind)
        food_stamps.pop(food_ind)
        make_food()

        SCORE += 1

        isGrow = True

        randColor = random.randint(0, len(color_list) - 1)
        
        snake.fillcolor(color_list[randColor])

        ## stamp_list.append(stamp)

    ## Don't eat yourself
    for i in range(len(pos_list) - 1):
        if pos_list[-1] == pos_list[i]:
            quit()
    
    turtle.ontimer(move_snake, TIME_STEP)

def printScore():
    global SCORE
    turtle.goto(-390, 170)
    turtle.color("lightblue")
    turtle.clear()
    turtle.write("Score: " + str(SCORE), False, "left", ("Julee", 16, "normal"))
    turtle.ontimer(printScore, 1000)

createBorder()
make_food()
move_snake()
printScore()
