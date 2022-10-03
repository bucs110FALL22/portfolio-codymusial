import random
import turtle

window = turtle.Screen()
myturtle = turtle.Turtle()
myturtle.shape('turtle')


coin = ["Heads", "Tails"]
flip = random.choice(coin)

if flip == "Heads":
  myturtle.left(90)
  myturtle.fd(50)

if flip == "Tails":
  myturtle.right(90)
  myturtle.fd(50)

