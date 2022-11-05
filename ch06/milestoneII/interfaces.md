# Final Project Milestone #2

[Final Project Description](https://docs.google.com/document/d/1j3zgypVjPjzXl4pL1_Wpjvp3GLCW9zcFydkwUjNfNUA/edit?usp=sharing)

Complete this document in **your** portfolio (CH 6). 

Let's decide on our Final project. Select the idea from Milestone 1 that seems the most interesting to you.

Each class is a model of some real world object. We often refer to data classes as the ***models*** in a GUI program. Your models represent your application data.

Given what you have learned about classes on Chapter 6, describe the ***interface only*** of 3 classes you think you might need for your project.

*For example*, if you want to create a space invaders type game, you would need a class to represent the ship, which could have an interface such as: 

* class ship
    * moveLeft()
    * moveRight()
    * shoot()

***

Come up with interfaces fot 3 possible classes you think you may need. Again, brainstorm a little. Nothing is *wrong*.

## Class Interface 1

class tiles:
  def __init__(self, picture, id):
    self.pic = picture
    self.id = id
  def _matches(self):
    1 = 4
    2 = 3

t1 = tiles('Bearcats', 1)
t2 = tiles('Blue Devils', 2)
t3 = tiles('Blue Devils', 3)
t4 = tiles('Bearcats', 4)

#60 more times to make an 8x8

## Class Interface 2

class Point(object):
  def__init__(self,x,y)
  self.X = x
  self.Y = y

  def move(self, dx,dy):
    self.X = self.X + dx
    self.Y = self.Y + dy
def test point(x=0,y=0):
p1 = point(x,y)
print(p1)
p2 = Point(x,0)
print(p2)


## Class Interface 3

import pygame
import time
pygame.init()

ck = pygame.display.set_mode((800,600)) 

pygame.display.set_caption("matching game") 

clock = pygame.time.Clock() 

start_ck = pygame.Surface(ck.get_size()) 

start_ck2 = pygame.Surface(ck.get_size()) 

start_ck = start_ck.convert()

start_ck2 = start_ck2.convert()

start_ck.fill((255,255,255))

start_ck2.fill((0,255,0))


n1 = True

while n1:
  clock.tick(30)
  buttons = pygame.mouse.get_pressed()

  x1, y1 = pygame.mouse.get_pos()

  if x1 >= 227 and x1 <= 555 and y1 >= 261 and y1 <=327:

    start_ck.blit(i11, (200, 240))

    if buttons[0]:

        n1 = False

      elif x1 >= 227 and x1 <= 555 and y1 >= 381 and y1 <=447:

start_ck.blit(i21, (200, 360))

if buttons[0]:

pygame.quit()

exit()

elif x1 >= 227 and x1 <= 555 and y1 >= 501 and y1 <=567:

start_ck.blit(i31, (200, 480))

else:

start_ck.blit(i1, (200, 240))

start_ck.blit(i2, (200, 360))

start_ck.blit(i3, (200, 480))

ck.blit(start_ck,(0,0))

pygame.display.update()
for event in pygame.event.get():

if event.type == pygame.QUIT:

print("quit the game")


pygame.quit()

exit()

ck.blit(start_ck2,(0,0))

pygame.display.update()


n2 = True

while n2:

clock.tick(30)

ck.blit(start_ck2, (0, 0))

start_ck2.blit(bg,(0,0))

pygame.display.update()

for event in pygame.event.get():

if event.type == pygame.QUIT:

print("quit game")

pygame.quit()

exit()
