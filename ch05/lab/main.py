import pygame
pygame.init()
display = pygame.display.set_mode()
display.fill("blue")
count = 0
upper_limit = 101
iters={}
x = []
y = []
max_so_far = 0
font = pygame.font.Font(None, 30)
for start in range(2,upper_limit+1,1):
  n = start
  count = 0
  while n>1:
    count = count+1
    if n%2==0:
      n = int(n/2)
      print(n)
    else:
      n = int(3*n+1)
      print(n)
  if count>max_so_far:
    max_so_far = count
  iters[start*5]=count*5
max_val = max_so_far
print(iters)
print(max_val)
coords = list(iters.items())

if len(iters)>1:
  graph = pygame.draw.lines(display, "black", False, coords,1)
  pygame.display.flip()
  pygame.time.wait(2000)
new_display =pygame.transform.flip(display, False, True)
tempString = "The largest number is " + str(max_val)
msg = font.render(tempString, True, "black")
display.blit(msg, (10,400))
pygame.display.update()
pygame.time.wait(2000)