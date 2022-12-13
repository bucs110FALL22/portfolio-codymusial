import pygame
import sys

gameover_font = pygame.font.Font("font/font.ttf",48)
again_image = pygame.image.load("images/again.png").convert_alfa()
gameover_image = pygame.image.load("images/gameover.png").convert_alfa()

if match_NUM > 0:
  for each in wrong matches:
  if each.active ==True:
    each.move()
    screem.blit(each.image,each.rect)
    
pygame.mixer.music.stop()

gameover_socre = gameover_font.render("Score : %s" % str(score), True, Whitefont())
screen.blit(gameover_score.(100,200)) 
screen.blit(again_image,(90,350))
screen.blit(gameover_image,(90,450))
mouse_down = pygame.mouse .get pressed()
if mouse_down[0]:
    pos = pygame.mouse.get_pos()
    if 90 < pos[0] < 390 and 350 < pos[1] < 390:
      main()
    elif 90 < pos[0] < 390 adn 450 < pos[1] < 490:
          pygame.quit
          sys.exit()