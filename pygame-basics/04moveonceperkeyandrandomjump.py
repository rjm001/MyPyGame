# this program lets you move the ball around the screen with the arrow keys
# it requires keystrokes to move the ball, and it moves the ball one pixel at a time. very painful
# 1 Import packages

import pygame
from pygame.locals import *
import sys
import random

# 2 Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
BALL_WIDTH_HEIGHT = 100
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT
TARGET_X = 400
TARGET_Y = 320 
TARGET_WIDTH_HEIGHT = 120
N_PIXELS_TO_MOVE = 3

# 3 initialize world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 load assets: images, sounds, etc.
ballImage = pygame.image.load("images/ball.png")
targetImage = pygame.image.load('images/target.jpg')

# 5 initialize variables
ballX = random.randrange(MAX_WIDTH)
ballY = random.randrange(MAX_HEIGHT)
ballRect = pygame.Rect(ballX, ballY, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)
targetRect = pygame.Rect(TARGET_X, TARGET_Y, TARGET_WIDTH_HEIGHT, TARGET_WIDTH_HEIGHT)
num_clicks = 0


# game
while True:
    # 7 Check for and handle events
    for event in pygame.event.get():
        # exits when click close button
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ballX = ballX - N_PIXELS_TO_MOVE
            elif event.key == pygame.K_RIGHT:
                ballX = ballX + N_PIXELS_TO_MOVE
            elif event.key == pygame.K_UP:
                ballY = ballY - N_PIXELS_TO_MOVE
            elif event.key == pygame.K_DOWN:
                ballY = ballY + N_PIXELS_TO_MOVE

        # see if user clicked
        elif event.type == pygame.MOUSEBUTTONUP:
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
    ballRect = pygame.Rect(ballX, ballY, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)
    if ballRect.colliderect(targetRect):
        print("Ball is touching target")

        # 9 clear window
    window.fill(BLACK)

        # draw all window elements
    window.blit(targetImage, (TARGET_X, TARGET_Y))
    window.blit(ballImage, (ballX, ballY)) #now position is a variable
        # update window
    pygame.display.update()

        # slow things down
    clock.tick(FRAMES_PER_SECOND)