import turtle #1. import modules
import random
import pygame
import math

#Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. Your PART A code goes here
for x in range(10):
  x = random.randrange(1,11)
  y = random.randrange(1,11)
  michelangelo.fd(x)
  leonardo.fd(y)

michelangelo.goto(-100,20)
leonardo.goto(-100,-20)
  
# PART B - complete part B here
pygame.init()
window = pygame.display.set_mode()
side_length = 50
offset = 100
coords = []
num_sides = 3
for i in range(num_sides):
  theta = (2 * math.pi * i)/ num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append([x,y])
pygame.draw.polygon(window, 'white', coords)
pygame.display.flip()
pygame.time.wait(1000)
window.fill('black')

num_sides = 4
coords.clear()
for i in range(num_sides):
  theta = (2 * math.pi * i)/ num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append([x,y])
pygame.draw.polygon(window, 'white', coords)
pygame.display.flip()
pygame.time.wait(1000)
window.fill('black')

num_sides = 6
coords.clear()
for i in range(num_sides):
  theta = (2 * math.pi * i)/ num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append([x,y])
pygame.draw.polygon(window, 'white', coords)
pygame.display.flip()
pygame.time.wait(1000)
window.fill('black')

num_sides = 9
coords.clear()
for i in range(num_sides):
  theta = (2 * math.pi * i)/ num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append([x,y])
pygame.draw.polygon(window, 'white', coords)
pygame.display.flip()
pygame.time.wait(1000)
window.fill('black')

num_sides = 360
coords.clear()
for i in range(num_sides):
  theta = (2 * math.pi * i)/ num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append([x,y])
pygame.draw.polygon(window, 'white', coords)
pygame.display.flip()
pygame.time.wait(1000)