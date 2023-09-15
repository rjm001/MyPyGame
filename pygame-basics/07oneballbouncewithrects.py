# this program lets you move the ball around the screen with the arrow keys
# it allows continuous keystrokes to move the ball, much faster than 04.
# you can click the ball and have it reappear in a random location
# the ball also has natural drift on its own
# You can drive the ball off screen, but it will come back on its
# this one lets the program infer the object's width and height from the image

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
TARGET_X = 400
TARGET_Y = 320
TARGET_WIDTH_HEIGHT = 120
N_PIXELS_TO_MOVE = 4
N_PIXELS_PER_FRAME = 3

# 3 initialize world
pygame.init()
window = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
clock = pygame.time.Clock()

# 4 load assets: images, sounds, etc.
ballImage = pygame.image.load("images/ball.png")
targetImage = pygame.image.load('images/target.jpg')
bounceSound = pygame.mixer.Sound('sounds/boing.wav')
pygame.mixer.music.load('sounds/background.mp3')
pygame.mixer.music.play(-1, 0.0) # args are (<number of loops>, <starting position>). -1 means loop forever, 0.0 means start at 0.0 seconds

# 5 initialize variables
#ballX = random.randrange(MAX_WIDTH)
#ballY = random.randrange(MAX_HEIGHT)
ballRect = ballImage.get_rect() #pygame.Rect(ballX, ballY, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT) now settting it
#BALL_WIDTH_HEIGHT = 100
MAX_WIDTH = WINDOW_WIDTH - ballRect.width
MAX_HEIGHT = WINDOW_HEIGHT - ballRect.height
ballRect.left = random.randrange(MAX_WIDTH)
ballRect.top = random.randrange(MAX_HEIGHT)
xSpeed = N_PIXELS_PER_FRAME
ySpeed = N_PIXELS_PER_FRAME


targetRect = pygame.Rect(TARGET_X, TARGET_Y, TARGET_WIDTH_HEIGHT, TARGET_WIDTH_HEIGHT)
num_clicks = 0


# 6 game
while True:
    # 7 Check for and handle events
    for event in pygame.event.get():
        # exits when click close button
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # see if user clicked (this is an event; vs keystrokes not events below because want to catch those every frame continuously)
        if event.type == pygame.MOUSEBUTTONUP:
            # mouseX, mouseY = event.pos #could do this if we wanted to
            # that is, event.pos returns the x and y coordinates where released mouse

            #@ check if the click was on the ball
            # <booleanVariable> = <rectVariable>.collidepoint(<someXYlocation>) 
            if ballRect.collidepoint(event.pos):
                num_clicks = num_clicks + 1
                print(f"You clicked the ball {num_clicks} times!")
                ballRect.left = random.randrange(MAX_WIDTH)
                ballRect.top = random.randrange(MAX_HEIGHT)
        

    # 8 do any per-frame actions

    ## 8A Inserting Drift
    if (ballRect.left<0):
        xSpeed = N_PIXELS_PER_FRAME
        bounceSound.play()
    elif (ballRect.right>WINDOW_WIDTH):
        xSpeed = -(N_PIXELS_PER_FRAME)
        bounceSound.play()
    if (ballRect.top<0):
        ySpeed = N_PIXELS_PER_FRAME
        bounceSound.play()
    elif (ballRect.bottom>WINDOW_HEIGHT):
        ySpeed = -(N_PIXELS_PER_FRAME)
        bounceSound.play()
    ballRect.left = ballRect.left + xSpeed
    ballRect.top = ballRect.top + ySpeed


    ## 8B Adding Keyboard Controls
    keyPressedTuple = pygame.key.get_pressed()
    if keyPressedTuple[pygame.K_LEFT]:
        ballRect.left = ballRect.left - N_PIXELS_TO_MOVE
        
    if keyPressedTuple[pygame.K_RIGHT]:
        ballRect.left = ballRect.left + N_PIXELS_TO_MOVE
        
    if keyPressedTuple[pygame.K_UP]:
        ballRect.top = ballRect.top - N_PIXELS_TO_MOVE
        
    if keyPressedTuple[pygame.K_DOWN]:
        ballRect.top = ballRect.top + N_PIXELS_TO_MOVE

    ## 8C Inserting Target
    #ballRect = pygame.Rect(ballX, ballY, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)
    if ballRect.colliderect(targetRect):
        print("Ball is touching target")

    # 9 clear window
    window.fill(BLACK)

        # draw all window elements
    window.blit(targetImage, (TARGET_X, TARGET_Y))
    window.blit(ballImage, ballRect) #now position is a variable
        # update window
    pygame.display.update()

        # slow things down
    clock.tick(FRAMES_PER_SECOND)