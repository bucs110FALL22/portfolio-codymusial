import random
import pygame

pygame.init()
screen = pygame.display.set_mode()

width, height = pygame.display.get_window_size() #  returns as a tuple of 2 items (w, h)

red = [200, 0, 0]
purple = [200, 0, 200]
green = [0, 200, 0]
blue = [0, 0, 200]

bright_red = [255, 0, 0]
bright_purple = [255, 0, 255]
bright_green = [0, 255, 0]
bright_blue = [0, 0, 255]

black = [0, 0, 0]

instructions = """
    UP: red
    DOWN: purple
    LEFT: green
    RIGHT: blue
"""

start_msg = "Press spacebar to play the game..."
direction = ["UP", "DOWN", "LEFT", "RIGHT"]

hit_box_width = width/3
hit_box_height = height/3

red_button_box = pygame.Rect(0,0, hit_box_width, hit_box_height)
purple_button_box = pygame.Rect(0,0, hit_box_width, hit_box_height)
blue_button_box = pygame.Rect(0,0, hit_box_width, hit_box_height)
green_button_box = pygame.Rect(0,0, hit_box_width, hit_box_height)

green_button_box.topright = red_button_box.bottomleft
blue_button_box.top_left = red_button_box.bottomright
purple_button_box.top_left = green_button_box.bottomright

red_button = pygame.draw.rect(screen, red, red_button_box)
green_button = pygame.draw.rect(screen, green, green_button_box)
blue_button = pygame.draw.rect(screen, blue, blue_button_box)
purple_button = pygame.draw.rect(screen, purple, purple_button_box)


lost = False
result = []
turns = 0

#each time through the white is one frame
while True:


# print("Simon says to enter the following sequence:")
# for i in direction:
#     if i == "UP":
#         screen.fill(red)
#     elif i == "DOWN":
#         screen.fill(purple)
#     elif i == "LEFT":
#         screen.fill(green)
#     elif i == "RIGHT":
#         screen.fill(blue)
#     pygame.display.flip()
#     pygame.time.wait(1000)
#     screen.fill(black)
#     pygame.display.flip()
#     pygame.time.wait(500)

# result = []

# input(
#     "Click on the window, enter the sequence, then press enter in the console:"
# )

# print("You pressed:")
# for event in pygame.event.get():
#     #print(event)
#     if event.type == pygame.KEYDOWN:
#         if (event.key == pygame.K_UP):
#             screen.fill(red)
#             result.append("UP")
#             print("UP")
#         elif (event.key == pygame.K_DOWN):
#             screen.fill(purple)
#             result.append("DOWN")
#             print("DOWN")
#         elif (event.key == pygame.K_LEFT):
#             screen.fill(green)
#             result.append("LEFT")
#             print("LEFT")
#         elif (event.key == pygame.K_RIGHT):
#             screen.fill(blue)
#             result.append("RIGHT")
#             print("RIGHT")
#         pygame.display.flip()
#         pygame.time.wait(1000)

# print("You Entered:", result)
# print("The correct pattern was", direction)
# if result == direction:
#     print("Correct! You win.")
# else:
#     print("Were you even paying attention?")
  