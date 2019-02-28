import turtle

def drawCard():
    turtle.down()
    turtle.fd(400)
    turtle.left(90)
    turtle.fd(280)
    turtle.left(90)
    turtle.fd(400)
    turtle.left(90)
    turtle.fd(280)
    turtle.left(90)
    turtle.up()

def drawTriangle():
    turtle.begin_fill()
    turtle.right(30)
    turtle.down()
    turtle.fd(40)
    turtle.left(120)
    turtle.fd(40)
    turtle.left(120)
    turtle.fd(40)
    turtle.up()
    turtle.left(150)
    turtle.end_fill()
    turtle.up()

def drawCircle():
    turtle.down()
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()
    turtle.up()

def drawDiamond():
    turtle.begin_fill()
    turtle.right(30)
    turtle.down()
    turtle.fd(30)
    turtle.left(60)
    turtle.fd(30)
    turtle.left(120)
    turtle.fd(30)
    turtle.left(60)
    turtle.fd(30)
    turtle.left(150)
    turtle.end_fill()
    turtle.up()

def main():
    turtle.pensize(2)
    turtle.pencolor("black")
    turtle.up()
    turtle.left(180)
    turtle.fd(50)
    turtle.left(90)
    turtle.fd(200)
    turtle.right(180)
    turtle.down() #all getting into starting position to draw card
    drawCard() #draws first card
    turtle.fd(140)
    turtle.left(90)
    turtle.fd(140)
    turtle.right(90) #centers turtle in order to write letter or number in center
    turtle.down()
    turtle.pencolor("red")
    turtle.write("K", align="center", font=( "Arial", 100, "bold")) #writes K
    turtle.up()
    turtle.fd(200)
    turtle.left(90)
    turtle.fd(120)
    turtle.right(90) #moves to top right corner to draw first diamond
    turtle.fillcolor("red")
    drawDiamond() #draws first diamond
    turtle.right(90)
    turtle.fd(240)
    turtle.right(90)
    turtle.fd(330)
    turtle.right(180)#moves to bottom left corner to draw second diamond
    drawDiamond() #draws second diamond
    turtle.right(180)
    turtle.fd(10)
    turtle.left(90)
    turtle.fd(390)
    turtle.left(90)#moves into position to draw second card
    turtle.down()
    turtle.pencolor("black") #change pen back to black
    drawCard() #draws second card
    turtle.fd(140)
    turtle.left(90)
    turtle.fd(140)
    turtle.right(90)  # centers turtle in order to write letter or number in center
    turtle.down()
    turtle.write("8", align="center", font=("Arial", 100, "bold"))  # writes 8
    turtle.up()
    turtle.fd(190)
    turtle.left(90)
    turtle.fd(100)
    turtle.right(90) #moves turtle to top right to draw first heart
    turtle.fillcolor("black")
    drawTriangle() #draws bottom of heart
    turtle.fd(40)
    drawCircle() #draws left bump of heart
    turtle.right(90)
    turtle.fd(20)
    turtle.left(90) #moves to right to do second bump on heart
    drawCircle() #draws second bump of heart
    turtle.right(90)
    turtle.fd(180)
    turtle.right(90)
    turtle.fd(350)
    turtle.right(180)
    drawTriangle()  # draws bottom of heart
    turtle.fd(40)
    drawCircle()  # draws left bump of heart
    turtle.right(90)
    turtle.fd(20)
    turtle.left(90)  # moves to right to do second bump on heart
    drawCircle()  # draws second bump of heart
    turtle.done()

main()