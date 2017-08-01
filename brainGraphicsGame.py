import turtle
import random

turtle.tracer(1, 0)

SIZE_X = 800
SIZE_Y = 500

UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400

turtle.setup(SIZE_X, SIZE_Y)
turtle.bgcolor("black")

turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 10

SPEED = 50

## Initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

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
        direction = UP #Change direction to up
        print("You pressed the up key!")

def down():
    global direction #snake direction is global (same everywhere)
    if direction != UP:
        direction = DOWN #Change direction to up
        print("You pressed the down key!")

def left():
    global direction #snake direction is global (same everywhere)
    if direction != RIGHT:
        direction = LEFT #Change direction to up
        print("You pressed the left key!")

def right():
    global direction #snake direction is global (same everywhere)
    if direction != LEFT:
        direction = RIGHT #Change direction to up
        print("You pressed the right key!")


#2. Make functions down(), left(), and right() that change direction
####WRITE YOUR CODE HERE!!
turtle.onkeypress(up, UP_ARROW)
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)# Create listener for up key
turtle.listen()

def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    
    if direction == RIGHT:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print("You moved Right!")

    elif direction == LEFT:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print("You moved Left!")

    elif direction == DOWN:
        snake.goto(x_pos, y_pos - SQUARE_SIZE)
        print("You moved Down!")

    elif direction == UP:
        snake.goto(x_pos, y_pos + SQUARE_SIZE)
        print("You moved Up!")

    #Stamp new element and append new stamp in list
    #Remember: The snake position changed - update my_pos()
    my_pos = snake.pos()
    pos_list.append(my_pos)

    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)
    ######## SPECIAL PLACE - Remember it for Part 5
    #pop zeroth element in pos_list to get rid of last the last
    #piece of the tail
    old_stamp = stamp_list.pop(0)
    snake.clearstamp(old_stamp)
    pos_list.pop(0)

    #Add new lines to the end of the function
    #Grab position of snake
    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]
    # The next three lines check if the snake is hitting the
    # right edge.

    ######## SPECIAL PLACE - Remember it for Part 5
    global food_stamps, food_pos
    #If snake is on top of food item
    if snake.pos() in food_pos:
        food_ind=food_pos.index(snake.pos()) #What does this do?
        food.clearstamp(food_stamps[food_ind]) #Remove eaten food stamp
        food_pos.pop(food_ind) #Remove eaten food position
        food_stamps.pop(food_ind) #Remove it
    
    if new_x_pos >= RIGHT_EDGE:
        print("You hit the right edge! Game over!")
        quit()

    elif new_x_pos <= LEFT_EDGE:
        print("You hit the right edge! Game over!")
        quit()

    elif new_y_pos >= UP_EDGE:
        print("You hit the right edge! Game over!")
        quit()

    elif new_y_pos <= DOWN_EDGE:
        print("You hit the right edge! Game over!")
        quit()

    turtle.ontimer(move_snake, TIME_STEP)

move_snake()
'''
def make_food():
    #The screen positions go from -SIZE/2 to +SIZE/2
    #But we need to make food pieces only appear on game squares
    #So we cut up the game board into multiples of SQUARE_SIZE.
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)-1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)+1
    #Pick a position that is a random multiple of SQUARE_SIZE
    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE
    ##1.WRITE YOUR CODE HERE: Make the food turtle go to the randomly-generated
    ## position
    food.goto(this_food_pos[0], this_food_pos[1])
    ##2.WRITE YOUR CODE HERE: Add the food turtle's position to the food positions list
    food_pos.append((food_x, food_y))
    ##3.WRITE YOUR CODE HERE: Add the food turtle's stamp to the food stamps list
    foodStamp = food.stamp()
    food_stamps.append(foodStamp)
    ##3.WRITE YOUR CODE HERE: Add the food turtle's stamp to the food stamps list



turtle.register_shape("trash.gif")
food = turtle.clone()
food.shape("trash.gif")
food.hideturtle()
#Locations of food
food_pos = [(100,100), (-100,100), (-100,-100), (100,-100)]
food_stamps = []
'''
# Write code that:
#1. moves the food turtle to each food position
#2. stamps the food turtle at that location
#3. saves the stamp by appending it to the food_stamps list using
# food_stamps.append( )
#4. Don’t forget to hide the food turtle!
'''
for this_food_pos in food_pos:
    food.goto(this_food_pos[0], this_food_pos[1])
    foodStamp = food.stamp()
    food_stamps.append(foodStamp)
    '''
