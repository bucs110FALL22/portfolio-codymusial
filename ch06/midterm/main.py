import turtle

def main():
  window = turtle.Screen()
  turtle.bgcolor("black")
  turtle.pensize(2)
  turtle.speed(0)
  draw_spirograph()

def draw_spirograph(firstcolor):
  for i in range(6):
    for colors in [firstcolor, "magenta", "blue", "cyan", "green", "yellow", "white"]:
      turtle.color(colors)
      turtle.circle(100)
      turtle.left(10)

draw_spirograph('red')
main()
turtle.hideturtle()
window.exitonclick()