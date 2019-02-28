"""
Tate Dyer
Lab4
"""

import turtle as t
import math

"""
function for the constant outer radius
"""
def r():
    return 300

"""
function to find the length of a side of any of the shapes, uses pythagoreum theorem
"""
def length_side(s,r):
    return math.sqrt((r * r) + (r * r) - (2 * (r * r) * math.cos(2 * math.pi / s)))

"""
function that finds the turn angle between each side of each shape
"""
def turn_angle(s):
    return 180-(180*(s-2)/s)

"""
function that find the new radius as the shapes go inward or decrease in sides
"""
def new_radius(s,r):
    return math.sqrt((r * r) - ((length_side(s,r) / 2) * (length_side(s,r) / 2)))
"""
moves turtle to initial position to begin drawing
"""
def init():
    t.hideturtle()
    t.speed("fastest")
    t.up()
    t.right(90)
    t.fd(r())
    t.left(90)

"""
draws each of the shapes with the specified number of sides and returns the lengths of the sides
"""
def draw_shape(s, r):
    n=s
    while(n>=1):
        t.down()
        t.fd(length_side(s, r))
        t.up()
        t.left(turn_angle(s))
        n=n-1
    return s*length_side(s,r)
"""
draws everything by knowing the number of shapes to be drawn and calling draw shape
for each and returns total sum of all shapes sides
draws circle in between each shape 
"""
def draw(n, r, sum):
    if n<3:
        return sum
    if n >= 3:
        t.down()
        t.circle(r)
        t.left(90 - (180 * (n - 2) / (2 * n)))
        t.down()
        colors(n)
        x=draw_shape(n,r)
        t.pencolor("black")
        t.up()
        t.fd(length_side(n,r)/2)
        return draw(n-1, new_radius(n,r), sum+x)

"""
function that allows alternating colors of each shape
"""
def colors(n):
    if( n%3==0):
        t.pencolor("red")
    elif(n%3==1):
        t.pencolor("green")
    else:
        t.pencolor("orange")

"""
a test for draw function
"""
def test_draw(s):
    draw(s,r(),0)

"""
a test for draw_shape function
"""
def test_draw_shape(s):
    draw_shape(s,r())

def main():
    while True:
        x=int((input("What is the number of sides for the largest shape? ")))
        if x<3:
            print("The number of sides you entered is out of range. Try again.")
            break
        else:
            print("The number of sides for the largest shape is", x)
            t.clear()
            t.reset()
            init()
            print("The distance around all of the polygons is ", draw(x,r(),0))

main()




