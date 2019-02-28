import turtle as t

def draw_cross_one(S):
    t.fd(S)
    t.fd(-S)
def draw_cross_two(S):
    t.fd(S)
    t.left(90)
    draw_cross_one(S/2)
    t.right(90)
    draw_cross_one(S / 2)
    t.right(90)
    draw_cross_one(S / 2)
    t.right(90)
    t.left(90)
    t.fd(-S)

def draw_cross_three(S):
    t.fd(S)
    t.left(90)
    draw_cross_two(S/2)
    t.right(90)
    draw_cross_two(S/2)
    t.right(90)
    draw_cross_two(S/2)
    t.left(90)
    t.fd(-S)

def draw_cross_rec(S,N):
    if N<=0:
        pass
    else:
        t.fd(S)
        t.left(90)
        draw_cross_rec(S / 2, N - 1)
        t.right(90)
        draw_cross_rec(S / 2, N - 1)
        t.right(90)
        draw_cross_rec(S / 2, N - 1)
        t.left(90)
        t.fd(-S)
length_of_segment = int (raw_input("What is the length of the line segment?"))
depth= int(raw_input("What is the depth of the recursion?"))
draw_cross_rec(length_of__segment, depth)
t.done()