# this program generates the ball in a random location on the screen, then moves it to a new random location when the user clicks on it.
import pygame
from pygame.locals import *
import sys
import random

BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
BALL_WIDTH_HEIGHT = 100
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT

# initialize world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# load assets
ballImage = pygame.image.load("images/ball.png")

# initialize variables
ballX = random.randrange(MAX_WIDTH)
ballY = random.randrange(MAX_HEIGHT)
ballRect = pygame.Rect(ballX, ballY, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)
num_clicks = 0



# game
while True:
    # 7 Check for and handle events
    for event in pygame.event.get():
        # exits when click close button
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        # see if user clicked
        
        if event.type == pygame.MOUSEBUTTONUP:
            # mouseX, mouseY = event.pos #could do this if we wanted to
            # that is, event.pos returns the x and y coordinates where released mouse

            #@ check if the click was on the ball
            # <booleanVariable> = <rectVariable>.collidepoint(<someXYlocation>)
            if ballRect.collidepoint(event.pos):
                num_clicks = num_clicks + 1
                print(f"You clicked the ball {num_clicks} times!")
                ballX = random.randrange(MAX_WIDTH)
                ballY = random.randrange(MAX_HEIGHT)
                ballRect = pygame.Rect(ballX, ballY, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)

    # 8 do any per-frame actions


    # 9 clear window
    window.fill(BLACK)

    # draw all window elements
    window.blit(ballImage, (ballX, ballY)) #now position is a variable
    # update window
    pygame.display.update()

    # slow things down
    clock.tick(FRAMES_PER_SECOND)