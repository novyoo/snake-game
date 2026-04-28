# Snake game in python :333

import turtle
import time
import random

delay = 0.13

# Setting up the screen / the window that pops up
screen = turtle.Screen()
screen.title("S N A K E  G A M E")
screen.bgpic("bg.gif")
screen.setup(width = 620, height = 620)
screen.tracer(0) #turns off animations on screen

# Register your PNG image
screen.addshape("bg.gif")
screen.addshape("snake_up.gif") #i made sum random on procreate :333
screen.addshape("snake_down.gif")
screen.addshape("snake_right.gif")
screen.addshape("snake_left.gif")
screen.addshape("food.gif")
screen.addshape("snake_body.gif")

# Head
head = turtle.Turtle()
head.speed(0) #fastest animation speed (there's like no slowdown)
head.shape("snake_up.gif")
head.penup()
head.goto(0,0)
head.direction = "stop"

segments = []

# Food
food = turtle.Turtle()
food.speed(0)
food.shape("food.gif")
food.penup()
food.goto(0,100)


# Functions for direction
def moves():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20) # moves by 20px each time

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
 
# Functions to change direction of the head
def going_up():
    if head.direction != "down":
        head.direction = "up"
        head.shape("snake_up.gif")

def going_down():
    if head.direction != "up":
        head.direction = "down"
        head.shape("snake_down.gif")

def going_right():
    if head.direction != "left":
        head.direction = "right"
        head.shape("snake_right.gif")

def going_left():
    if head.direction != "right":
        head.direction = "left"
        head.shape("snake_left.gif")

# Adding Keybinds :33
screen.listen()
screen.onkeypress(going_up, "w")
screen.onkeypress(going_up, "Up")

screen.onkeypress(going_down, "s")
screen.onkeypress(going_down, "Down")

screen.onkeypress(going_right, "d")
screen.onkeypress(going_right, "Right")

screen.onkeypress(going_left, "a")
screen.onkeypress(going_left, "Left")

# Main game loop, this repeats over and over again
while True:
    screen.update()

    #check for collision with border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        #Hiding the segments
        for segment in segments:
            segment.goto(1000, 1000)

        segments.clear()

    if head.distance(food) < 30:
        
        # Move food to random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)
    
        #growth of the snake
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("snake_body.gif")
        new_segment.penup()
        segments.append(new_segment)
    
    # Movinf the parts
    for index in range(len(segments)-1, 0, -1):
        x = segments[index -1].xcor()
        y = segments[index -1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    moves()

    #check for head collisions w body
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            #Hiding the segments
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()

    time.sleep(delay)




screen.mainloop()
