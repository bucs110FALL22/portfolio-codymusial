import turtle

CIRCLE_DEG = 360

wn = turtle.Screen()

michelangelo = turtle.Turtle()
michelangelo.shape('turtle')

sides = 4  #no magic numbers
length = 50
#list of colors that the turtle will use

michelangelo.color("purple")
#move the turtle forward by length
michelangelo.forward(length)
# caluclate the angle of the turn,
# and change the turtle heading
michelangelo.left(CIRCLE_DEG / sides)
michelangelo.forward(length)
michelangelo.left(CIRCLE_DEG / sides)
michelangelo.forward(length)
michelangelo.left(CIRCLE_DEG / sides)
michelangelo.forward(length)
michelangelo.left(CIRCLE_DEG / sides)

michelangelo.up()
michelangelo.forward(100)
michelangelo.down()

michelangelo.color("red")

michelangelo.forward(length)
michelangelo.left(CIRCLE_DEG / sides)
michelangelo.forward(length)
michelangelo.left(CIRCLE_DEG / sides)
michelangelo.forward(length)
michelangelo.left(CIRCLE_DEG / sides)
michelangelo.forward(length)
michelangelo.left(CIRCLE_DEG / sides)

wn.exitonclick()