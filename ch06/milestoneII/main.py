import random
import pygame
import time
import tkinter

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
    