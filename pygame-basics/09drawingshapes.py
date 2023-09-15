# this program lets you move the ball around the screen with the arrow keys
# it allows continuous keystrokes to move the ball, much faster than 04.
# you can click the ball and have it reappear in a random location
# the ball also has natural drift on its own
# You can drive the ball off screen, but it will come back on its

# 1 Import packages
import pygame
from pygame.locals import *
import sys
import random

# 2 Define constants
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
TEAL = (0, 128, 128)
GREEN = (0, 255, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
BALL_WIDTH_HEIGHT = 100
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT
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

# 5 initialize variables
ballX = random.randrange(MAX_WIDTH)
ballY = random.randrange(MAX_HEIGHT)
xSpeed = N_PIXELS_PER_FRAME
ySpeed = N_PIXELS_PER_FRAME
ballRect = pygame.Rect(ballX, ballY, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)
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
                ballX = random.randrange(MAX_WIDTH)
                ballY = random.randrange(MAX_HEIGHT)
                ballRect = pygame.Rect(ballX, ballY, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)
        

    # 8 do any per-frame actions

    ## 8A Inserting Drift
    if (ballX<0):
        xSpeed = N_PIXELS_PER_FRAME
    elif (ballX>MAX_WIDTH):
        xSpeed = -(N_PIXELS_PER_FRAME)
    if (ballY<0):
        ySpeed = N_PIXELS_PER_FRAME
    elif (ballY>MAX_HEIGHT):
        ySpeed = -(N_PIXELS_PER_FRAME)
    ballX = ballX + xSpeed
    ballY = ballY + ySpeed


    ## 8B Adding Keyboard Controls
    keyPressedTuple = pygame.key.get_pressed()
    if keyPressedTuple[pygame.K_LEFT]:
        ballX = ballX - N_PIXELS_TO_MOVE
        
    if keyPressedTuple[pygame.K_RIGHT]:
        ballX = ballX + N_PIXELS_TO_MOVE
        
    if keyPressedTuple[pygame.K_UP]:
        ballY = ballY - N_PIXELS_TO_MOVE
        
    if keyPressedTuple[pygame.K_DOWN]:
        ballY = ballY + N_PIXELS_TO_MOVE

    ## 8C Inserting Target
    ballRect = pygame.Rect(ballX, ballY, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)
    if ballRect.colliderect(targetRect):
        print("Ball is touching target")

    # 9 clear window
    window.fill(GRAY)

    # 10 draw all window elements
    ## 10a draw images
    window.blit(targetImage, (TARGET_X, TARGET_Y))
    window.blit(ballImage, (ballX, ballY)) #now position is a variable
    
    ## 10b draw a box


    ## 10c Draw an X in the box


    ## 10cc Draw a filled and empty circle

    ## 10d Draw a filled and empty rectangle
    #pygame.draw.rect(window, color, rect (can be as a 4-ple), width=0) #0 width = filled
    pygame.draw.rect(window, GREEN, (250, 150, 100, 50), 0) # filled
    pygame.draw.rect(window, GREEN, (400, 150, 100, 50), 2) # 2 pixel edge


    ## 10e draw a filled and empty ellipse
    #pygame.draw.ellipse(window, color, rect (can be as a 4-ple), width=0) #0 width = filled
    pygame.draw.ellipse(window, RED, (250, 250, 80, 40), 0) # filled
    pygame.draw.ellipse(window, RED, (400, 250, 80, 40), 1) # 1 pixel edge


    ## 10f drawa six-sided poplygon
    #pygame.draw.polygon(window. cp;pr. pointslist, width (in pixels) = 0) #0 width = filled
    pygame.draw.polygon(window, TEAL, ((240, 350), (350, 350), (410, 410), (350, 470), (240, 470), (180, 410)), 0) #0 is filled

    ## 10g draw an arc
    #pygame.draw.arc(window, color, rect (can be as a 4-ple), angle_start, angle_stop, width=0)
    pygame.draw.arc(window, BLUE, (20, 400, 100, 100), 0, 2, 5)

    ## 10h draw anti-aliased lines: a single line then a list of points. anti-aliased means blended colors at the endges to make the lines look smoother
    # pygame.draw.aaline(window, color, startpos, endpos, blend=True) #or
    # pygame.draw.aalines(window, color, closed, points, blend=True)
    pygame.draw.aaline(window, RED, (200, 400), (WINDOW_WIDTH, WINDOW_HEIGHT), 1)
    pygame.draw.aalines(window, BLUE, True, ((580, 400), (587, 450), (595, 460),(600,444)), 1)

    # 11 update window
    pygame.display.update()

    # 12 slow things down
    clock.tick(FRAMES_PER_SECOND)