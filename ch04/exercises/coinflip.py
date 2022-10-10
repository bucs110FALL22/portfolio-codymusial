import random
import turtle

window = turtle.Screen()
myturtle = turtle.Turtle()
myturtle.shape('turtle')
myturtle.speed(0)

distance = 10
angle = 90

colors = ["green", "blue", "purple"]

is_in_screen = True

while is_in_screen:
  coin = random.randrange(0,2)
  if coin == 0:
    myturtle.left(angle)
  else:
    myturtle.right(angle)
    myturtle.fd(10)
  
  turtleX = myturtle.xcor()
  turtleY = myturtle.ycor()
  
  x_range = window.window_width()/2
  y_range = window.window_height()/2

  myturtle.color(colors[0])
  colors.append(colors.pop(0))
  if abs(turtleX) > x_range or abs(turtleY) > y_range:
    is_in_screen = False

window.bgcolor("yellow")
window.exitonclick()