# -----------------------------------------------------------------------------
# Roomba in Python
# This file implements an algorithm for a roomba cleaning a room.
#
# Author: Dr. EB <------ REPLACE THIS WITH YOUR NAME!
# -----------------------------------------------------------------------------
 
from turtle import right, left, forward, backward, speed
import room

# Make the turtle go faster
speed(6)

# Draw the Level 3 version of the room
window = room.draw_room(level = 3, radius = 5)

###
# Start your code here
forward(400)
backward(40)
right(90)
forward(40)
right(90)
forward(320)
left(90)
forward(40)
left(90)
forward(320)
right(90)
forward(40)
right(90)
forward(320)
backward(40)
left(90)
forward(40)
left(90)
forward(240)
backward(120)
right(90)
forward(40)
right(180)
forward(240)
left(90)
forward(160)
backward(320)
right(90)
forward(40)
left(90)
forward(320)
right(90)
forward(40)
right(90)
forward(320)
backward(40)
left(90)
forward(40)
left(90)
forward(240)
backward(120)
right(90)
forward(40)


 
 
# End your code here
###
 
window.exitonclick()