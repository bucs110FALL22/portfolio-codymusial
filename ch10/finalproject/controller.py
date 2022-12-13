import pygame
import sys
import datetime

from easy import easy
from medium import medium
from hard import hard

class Controller():
  def __init__(self):
    self.clock = pygame.time.Clock()
    self.time = 20000


  def timeDisplay(self):
    seconds = self.time//1000
    minutes = seconds//60
    seconds = seconds % 60

    time = self.gameFont.render(f"Time left -Minutes: {minutes} Seconds: {seconds} " , False, (255, 255, 0))
    self.screen.blit(time, (0,0))




  def game_loop(self):
    self.timeDisplay()



    
  # if select == "easy":easy()
  #   if select == "medium":medium()
  #     if select == "hard":hard()

def main():
  controller.run()

main()