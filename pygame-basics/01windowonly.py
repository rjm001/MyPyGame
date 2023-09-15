import pygame
from pygame.locals import *
import sys

BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

# initialize world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# load assets
# initialize variables
# game
while True:
    # Check for and handle events
    for event in pygame.event.get():
        # exits when click close button
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
    # do any per-frame actions

    # clear window
    window.fill(BLACK)

    # draw all window elements
    # update window
    pygame.display.update()

    # slow things down
    clock.tick(FRAMES_PER_SECOND)