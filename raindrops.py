"""
Tate Dyer
Lab 3
"""

import turtle as t
import math
import random

"""
sets the radius of the window as a function that be called anytime it's needed throughout the program
"""
def p():
    return 250

"""
sets max amount of raindrops allowed to input to be called in program later
"""
def max_raindrops():
    return 100

"""
sets max amount of raindrops allowed to input to be called in program later
"""
def max_radius():
    return 15

"""
sets constant amount of ripples to be called in program later
"""
def ripples():
    return 5

"""
draws the pond or the square that bounds the raindrops
"""
def pond ():
    t.up()
    t.right(90)
    t.fd(p())
    t.left(90)
    t.down()
    t.fillcolor(105/255,190/255,1)
    t.begin_fill()
    t.fd(p())
    t.left(90)
    t.fd(2*p())
    t.left(90)
    t.fd(2*p())
    t.left(90)
    t.fd(2*p())
    t.left(90)
    t.fd(p())
    t.end_fill()
    t.up()

"""
draws a single raindrop anytime it is called and returns the circumference of the raindrop
"""
def raindrop():
    rad=random.randint(1, max_radius())
    t.penup()
    t.setpos(random.randint((-p()+rad*(ripples()+1)), (p()-rad*(ripples()+1))), random.randint((-p()+rad*(ripples()+1)), (p()-rad*(ripples()+2))))
    t.pendown()
    t.begin_fill()
    t.fillcolor(random.random(), random.random(), random.random())
    t.circle(rad)
    t.end_fill()
    t.pencolor("black")
    return draw_ripples(2*rad, rad, ripples(),0)


"""
non-tail recursive function to draw multiple raindrops and return the total circumference of them all
n= number of raindrops
"""
def draw_raindrops(n):
    if n<=0:
        return 0
    elif(n>max_raindrops()):
        print("That number is too high.")
    else:
        return raindrop() + draw_raindrops(n - 1)

"""
tail recursive function to add the ripples to each raindrop
r=the radius which changes to create ripples, ir=initial radius
to keep constant to use for the gap between each ripple, n=number of ripples,
acc= the accumulation of all the circumferences of the ripples to be addded to the raindrops for a total
"""

def draw_ripples(r, ir,  n=ripples(), acc=0):
    if n<=0:
        return acc
    else:
        t.penup()
        t.right(90)
        t.fd(ir)
        t.left(90)
        t.pendown()
        t.circle(r)
        return draw_ripples((r+ir), ir,  n-1, acc+2*r*math.pi)

def main():
    t.speed("fastest")
    t.hideturtle()
    pond()
    print("Circumference: ", draw_raindrops(int(input("Please enter the number of raindrops. "))))
    t.done()

main()