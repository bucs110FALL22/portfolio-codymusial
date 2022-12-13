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

    t1 = tiles('Bearcats', 1)
    t2 = tiles('Blue Devils', 2)
    t3 = tiles('Blue Devils', 3)
    t4 = tiles('Bearcats', 4)
    t5 = tiles('Bulldogs', 5)
    t6 = tiles('UCLA', 6)
    t7 = tiles('Clemson', 7)
    t8 = tiles('Texas', 8)
    t9 = tiles('Oregon', 9) 
    t10 = tiles('Hofstra', 10) 
    t11 = tiles('Michigan', 11) 
    t12 = tiles('Florida Gators', 12) 
    t13 = tiles('South Carolina', 13) 
    t14 = tiles('Purdue', 14) 
    t15 = tiles('Army', 15) 
    t16 = tiles('Arkansas', 16) 
    t17 = tiles('Ole Miss', 17) 
    t18 = tiles('Fighting Irish', 18) 
    t19 = tiles('Georgia', 19) 
    t20 = tiles('UAlbany', 20) 
    t21 = tiles('Texas Tech', 21) 
    t22 = tiles('UCLA', 22) 
    t23 = tiles('Kentucky', 23) 
    t24 = tiles('Michigan State', 24) 
    t25 = tiles('UMiami', 25) 
    t26 = tiles('Bulldogs', 26) 
    t27 = tiles('Tennesee', 27) 
    t28 = tiles('Boston College', 28) 
    t29 = tiles('Boston College', 29) 
    t30 = tiles('Tar Heels', 30) 
    t31 = tiles('LSU', 31) 
    t32 = tiles('Florida Gators', 32) 
    t33 = tiles('Kentucky', 33) 
    t34 = tiles('Penn State', 34) 
    t35 = tiles('Purdue', 35) 
    t36 = tiles('Ohio State', 36) 
    t37 = tiles('Georgia', 37) 
    t38 = tiles('Rutgers', 38) 
    t39 = tiles('Navy', 39) 
    t40 = tiles('Arkansas', 40) 
    t41 = tiles('Army', 41) 
    t42 = tiles('Rutgers', 42) 
    t43 = tiles('Blue Hens', 43) 
    t44 = tiles('Texas Tech', 44) 
    t45 = tiles('Texas', 45) 
    t46 = tiles('UAlbany', 46) 
    t47 = tiles('Clemson', 47) 
    t48 = tiles('South Carolina', 48) 
    t49 = tiles('Navy', 49) 
    t50 = tiles('Ole Miss', 50) 
    t51 = tiles('Hofstra', 51) 
    t52 = tiles('UMiami', 52) 
    t53 = tiles('LSU', 53) 
    t54 = tiles('Penn State', 54) 
    t55 = tiles('Blue Hens', 55) 
    t56 = tiles('Syracuse', 56) 
    t57 = tiles('Michigan State', 57) 
    t58 = tiles('Tennesee', 58) 
    t59 = tiles('Fighting Irish', 59) 
    t60 = tiles('Ohio State', 60) 
    t61 = tiles('Michigan', 61) 
    t62 = tiles('Oregon', 62) 
    t63 = tiles('Tar Heels', 63) 
    t64 = tiles('Syracuse', 64) 
    
  def _matches(self):
    1 = 4
    2 = 3
    5 = 26
    6 = 22
    7 = 47
    8 = 45
    9 = 62
    10 = 51
    11 = 61
    12 = 32
    13 = 48
    14 = 35
    15 = 41
    16 = 40 
    17 = 50 
    18 = 59
    19 = 37
    20 = 46
    21 = 44
    23 = 33
    24 = 57
    25 = 52
    27 = 58
    28 = 29
    30 = 63
    31 = 53
    34 = 54
    36 = 60
    38 = 42
    39 = 49
    43 = 55
    56 = 64


#comparison between two tiles clicked, t1 = t7, False, False = +1 misclick
#if true tiles stay flipped
#need to import random

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
