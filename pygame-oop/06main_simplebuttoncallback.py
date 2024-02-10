# 1 - Import Packages
import pygame
from pygame.locals import *
import sys
import random
#from simpletext import *
from simplebutton import *

# 2 - Define Constants
N_BALLS = 3
N_BUTTONS = 3
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 100
FRAMES_PER_SECOND = 30

def myCallBackFunction():
    print("User pressed Button B, called myCallBackFunction()")

class CallBackTest():
    def __init__(self):
        pass
    def myMethod(self):
        print("User pressed Button C, called myMethod of the CallBackTest object")


# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Load Assets: images, sounds, etc.

# 5 - Initialize variables
oCallBackTest = CallBackTest()
oButtonA = SimpleButton(window, (25, 30), 'images/buttonAUp.png', 'images/buttonADown.png')
oButtonB = SimpleButton(window, (150, 30), 'images/buttonBUp.png', 'images/buttonBDown.png', callBack=myCallBackFunction) #passing it a function
oButtonC = SimpleButton(window, (275, 30), 'images/buttonCUp.png', 'images/buttonCDown.png', callBack=oCallBackTest.myMethod) #passing it the method from oCallBackTest

counter=0

# 6 - Game Loop
while True:
    #7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
        if oButtonA.handleEvent(event):
            print("User pressed Button A")

        # since oButttonB and oButtonC have callbacks, don't need to check result of these calls
        oButtonB.handleEvent(event)
        oButtonC.handleEvent(event)

    # 8 - 'Do any per-frame actions
    counter += 1

    # 9 - Clear window before drawing again
    # Note, if didn't do this, would have the ball leave a trail
    window.fill(GRAY)

    # 10 - Draw all window elements
    oButtonA.draw()
    oButtonB.draw()
    oButtonC.draw()

    # 11 - Update window
    pygame.display.update()


    # 12 - Adjust FPS
    clock.tick(FRAMES_PER_SECOND)