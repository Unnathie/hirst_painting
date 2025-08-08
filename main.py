import turtle
import random
import colorgram
from turtle import Turtle, Screen

# ================================
# STEP 1: Extract colors from image
# ================================
# Uncomment this section if you want to generate your own color list
# colors = colorgram.extract('spotpainting.jpg', 35)
# color_list = []
# for col in colors:
#     r = col.rgb[0]
#     g = col.rgb[1]
#     b = col.rgb[2]
#     color_list.append((r, g, b))
# print(color_list)

# Hardcoded color list from extracted image
color_list = [
    (202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), 
    (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), 
    (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), 
    (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), 
    (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), 
    (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), 
    (107, 127, 153), (174, 94, 97), (176, 192, 209)
]

# ================================
# STEP 2: Turtle Setup
# ================================
turtle.colormode(255)
timmy = Turtle()
timmy.hideturtle()
timmy.penup()
timmy.speed("fastest")

# Start position
timmy.teleport(-200, -200)

# ================================
# STEP 3: Draw the painting
# ================================
for _ in range(10):
    posx1 = timmy.xcor()
    posy1 = timmy.ycor()
    for _ in range(10):
        timmy.color(random.choice(color_list))
        timmy.dot(20)
        timmy.forward(50)
    timmy.teleport(posx1, posy1 + 50)

Screen().exitonclick()
