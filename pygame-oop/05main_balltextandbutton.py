# 1 - Import Packages
import pygame
from pygame.locals import *
import sys
import random
from ball import *
from randombutton import *
from simpletext import *
from simplebutton import *

# 2 - Define Constants
N_BALLS = 3
N_BUTTONS = 3
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
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
for oBallCnt in range(0, N_BALLS):
    oBall = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)
    ballList.append(oBall)
buttonList = []
for oButtonCnt in range(0, N_BUTTONS):
    oButton = RandomButton(window, WINDOW_WIDTH, WINDOW_HEIGHT, 'images/buttonUp.png', 'images/buttonDown.png', oButtonCnt)
    buttonList.append(oButton)
oFrameCountLabel = SimpleText(window, (60, 20), 'Program has run through this many loops: ', WHITE)
oFrameCountDisplay = SimpleText(window, (500, 20), '', WHITE)
oRestartButton = SimpleButton(window, (280, 60), 'images/restartUp.png', 'images/restartDown.png')
framecounter = 0

# 6 - Game Loop
while True:
    #7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    for oButton in buttonList:
        if oButton.handleEvent(event):
            buttonNumber = oButton.getNumber()
            print(f"Button {buttonNumber} clicked!")
            # reset all balls, for example
            for oBall in ballList:
                oBall.reset()

    if oRestartButton.handleEvent(event):
        framecounter = 0    
        
    # 8 - Do any per-frame actions
    for oBall in ballList:
        oBall.update()

    framecounter += 1
    oFrameCountDisplay.setValue(str(framecounter))

    # 9 - Clear window before drawing again
    # Note, if didn't do this, would have the ball leave a trail
    window.fill(BLACK)

    # 10 - Draw all window elements
    for oBall in ballList:
        oBall.draw()
    
    for oButton in buttonList:
        oButton.draw()

    oFrameCountLabel.draw()
    oFrameCountDisplay.draw()
    oRestartButton.draw()

    # 11 - Update window
    pygame.display.update()


    # 12 - Adjust FPS
    clock.tick(FRAMES_PER_SECOND)