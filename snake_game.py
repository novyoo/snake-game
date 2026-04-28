#snake game in python

import turtle

#setting up the screen / the window that pops up
screen = turtle.Screen()
screen.title("S N A K E  G A M E")
screen.bgcolor("LightBlue1")
screen.setup(width = 700, height = 700)
screen.tracer(0) #turns off animations on screen

# Register your PNG image
screen.addshape("snake_head.gif")

head = turtle.Turtle()
head.speed(0) #fastest animation speed (there's like no slowdown)
head.shape("snake_head.gif")
head.penup()
head.goto(0,0)
head.direction = "stop"

#Main game loop, this repeats over and over again
while True:
    screen.update()

screen.mainloop()
