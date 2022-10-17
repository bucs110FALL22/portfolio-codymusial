import pygame
import random
import math

pygame.init()
screen = pygame.display.set_mode()
(width,height) = pygame.display.get_window_size()
screen.fill("blue")
pygame.draw.circle(screen, "pink", (width/2, height/2), 150)
pygame.display.flip()
pygame.draw.line(screen, "black", (0, height/2), (width, height/2), 1)
pygame.draw.line(screen, "black", (width/2, 0), (width/2, height), 1)
pygame.display.flip()

count = 0
while (count < 10):
  count = count + 1
  x1 = random.randrange(0,width)
  y1 = random.randrange(0,height)
  distance_from_center = math.hypot(x1-width/2, y1-height/2)
  pygame.display.flip()
  if distance_from_center <= 150:
    pygame.draw.circle(screen, "green",(x1,y1), 5)
    pygame.time.wait(500)
    pygame.display.flip()
  else:
    pygame.draw.circle(screen, "red",(x1,y1), 5)
    pygame.time.wait(500)
    pygame.display.flip()
pygame.time.wait(3000)
print (count)
screen = pygame.display.set_mode()
(width,height) = pygame.display.get_window_size()
screen.fill("blue")

purpleSquare = pygame.draw.rect(screen,"purple",(171,131,60,60))
yellowSquare = pygame.draw.rect(screen,"yellow",(291,131,60,60))
pygame.display.flip()
print("Who do you think will win")
x = ""
pygame.time.wait(2000)
a,b = pygame.mouse.get_pos()
if 171 < a < 231 and 131 < b < 191 and pygame.MOUSEBUTTONDOWN:
  print("Okay, purple!")
  pygame.display.flip()
  x = "purple"
if 291 < a < 351 and 131 < b < 191 and pygame.MOUSEBUTTONDOWN:
  print("Okay, yellow!")
  pygame.display.flip()
  x = "yellow"
pygame.time.wait(2000)

screen = pygame.display.set_mode()
(width,height) = pygame.display.get_window_size()
screen.fill("blue")
pygame.draw.circle(screen, "pink", (width/2, height/2), 150)
pygame.display.flip()
pygame.draw.line(screen, "black", (0, height/2), (width, height/2), 1)
pygame.draw.line(screen, "black", (width/2, 0), (width/2, height), 1)
pygame.display.flip()
pygame.time.wait(2000)

pointsy = 0
pointsp = 0
count = 1

while (count < 10):
  count = count + 1
  x3 = random.randrange(0,width)
  y3 = random.randrange(0,height)
  distance_from_center = math.hypot(x3-width/2, y3-height/2)
  pygame.display.flip
  if distance_from_center <= 150:
    pygame.draw.circle(screen, "yellow",(x3,y3), 5)
    pointsy = pointsy + 1
    pygame.display.flip()
  else:
    pygame.draw.circle(screen, "red", (x3,y3), 5)
    pygame.time.wait(500)
  pygame.display.flip()
  pygame.time.wait(1000)
  x4 = random.randrange(0,width)
  y4 = random.randrange(0,height)
  distance_from_center = math.hypot(x4-width/2, y4-height/2)
  if distance_from_center <= 150:
    pygame.draw.circle(screen, "purple", (x4,y4), 5)
    pointsp = pointsp + 1
    pygame.display.flip()
    pygame.time.wait(500)
  else:
    pygame.draw.circle(screen, "red",(x4,y4), 5)
    pygame.time.wait(500)
  pygame.time.wait(1000)

if pointsy<pointsp :
  print("Purple wins!")
  if x == "purple":
    print("You were right!")
  else:
    print("You were wrong.")
if pointsy>pointsp :
  print("Yellow wins!")
  if x == "yellow":
    print("You were right")
  else:
    print("You were wrong.")
if pointsy==pointsp:
  print("It was a tie!")

pygame.display.flip()
pygame.time.wait(2000)
