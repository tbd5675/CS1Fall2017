import turtle as t
import math
import random

def init(r):
    t.pencolor("blue")


def draw_rings(r, depth, accu=0):
    if depth<=0:
        return accu


    else:
        t.penup()
        t.fd(r)
        t.left(90)
        t.pendown()
        t.circle(r)
        t.penup()
        t.right(90)
        draw_rings(r // 2, depth - 1, accu + (2 * r * math.pi))
        t.penup()
        t.left(180)
        t.fd(2*r)
        t.right(90)
        t.pendown()
        t.circle(r)
        t.penup()
        t.left(90)


def main():
    rad= int(input("Enter integer radius:"))
    d= int(input("Enter depth of recursion"))
    init(rad)
    print("Drew total distance of ", draw_rings(rad,d, d))
    print("CLose canvas window to quit.")
    t.done()
main()