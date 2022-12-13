import sys,pygame
pygame.init()


pygame.init()
size = width,height = 600,480

screen = pygame.display.set_mode(size)
pygame.display.set_caption("matching game")
QUIT = pygame.quit 
K_ESCAPE = pygame.quit
KEYUP = pygame.KEYUP
def checkfor_keypress():
  if len(pygame.event.get(QUIT)) > 0:
    pygame.quit()
    sys.exit()

    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents) ==0:
      return None
  
    elif keyUpEvents[0] ==K_ESCAPE:
      pygame.quit()
      sys.exit()
  else:
    return keyUpEvents[0].key

def showstartscreen():
  font = pygame.font.Font("anna.ttf",100)
  start_text=font.render("Matching game",True,(255,0,0))
  text_width,text_height=start_text.get_size()
  while True:
    screen.fill((124,205,124))
    screen.blit(start_text,((width-text_width)/2,(height-text_height)/2))
    if checkfor_keypress():
        pygame.event.get()
        return



def draw_press_key_msg():
    basicfont=pygame.font.Font("anna.ttf",30)
    pressKeySurf = basicfont.render('Press a key to play.', True,(40,40,40))
    presstext_width,presstext_height = pressKeySurf.get_size()
    screen.blit(pressKeySurf,(width-presstext_width)/2,(height-presstext_height)/2+150)

def showstartscreen():
    font=pygame.font.Font("anna.ttf,100")
    start_text=font.render("matching game",True,(255,0,0))
    text_width,text_height=start_text.get_size()
    while True:
        screen.fill((124,205,124))
        screen.blit((start_text,(width-text_width)/2,height-text_height/2))
        draw_press_key_msg()
        if checkfor_keypress():
          pygame.event.get()
          return

        pygame.display.update()
