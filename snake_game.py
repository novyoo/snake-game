# Snake game in python :333

import turtle
import time
import random

delay = 0.15

# Setting up the screen / the window that pops up
screen = turtle.Screen()
screen.title("S N A K E  G A M E")
screen.bgcolor("LightBlue1")
screen.setup(width = 600, height = 600)
screen.tracer(0) #turns off animations on screen

# Register your PNG image
screen.addshape("snake_up.gif") #i made sum random on procreate :333
screen.addshape("snake_down.gif")
screen.addshape("snake_right.gif")
screen.addshape("snake_left.gif")
screen.addshape("food.gif")

# Head
head = turtle.Turtle()
head.speed(0) #fastest animation speed (there's like no slowdown)
head.shape("snake_up.gif")
head.penup()
head.goto(0,0)
head.direction = "stop"

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
    head.direction = "up"
    head.shape("snake_up.gif")

def going_down():
    head.direction = "down"
    head.shape("snake_down.gif")

def going_right():
    head.direction = "right"
    head.shape("snake_right.gif")

def going_left():
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

    if head.distance(food) < 20:
        
        # Move food to random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

    moves()

    time.sleep(delay)




screen.mainloop()
