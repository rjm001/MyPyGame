# 1 - Import Packages
import pygame
from pygame.locals import *
import sys
import random
from ball import *
from simplebutton import *

# 2 - Define Constants
N_BALLS = 3
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Load Assets: images, sounds, etc.

# 5 - Initialize variables
ballList = []
for oBallcnt in range(0, N_BALLS):
    oBall = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)
    ballList.append(oBall)
oButton = SimpleButton(window, (150, 30), 'images/buttonUp.png', 'images/buttonDown.png')


# 6 - Game Loop
while True:
    #7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    if oButton.handleEvent(event):
        print("Button clicked!")
        # reset all balls, for example
        for oBall in ballList:
            oBall.reset()
    
        
    # 8 - Do any per-frame actions
    for oBall in ballList:
        oBall.update()

    # 9 - Clear window before drawing again
    # Note, if didn't do this, would have the ball leave a trail
    window.fill(BLACK)

    # 10 - Draw all window elements
    for oBall in ballList:
        oBall.draw()
    
    oButton.draw()

    # 11 - Update window
    pygame.display.update()


    # 12 - Adjust FPS
    clock.tick(FRAMES_PER_SECOND)