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
ballImage = pygame.image.load("images/ball.png")

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
    window.blit(ballImage, (0,0)) #in upper left
    window.blit(ballImage, (100, 200)) #somewhere else; so 2 images
        # measures from upper left corner
        # note taht python knows how big the object is, so only need starting location

    # update window
    pygame.display.update()

    # slow things down
    clock.tick(FRAMES_PER_SECOND)