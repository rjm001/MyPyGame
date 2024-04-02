# Balloon Game Main Code

# 1 - Import packages
from pygame.locals import *
import pygwidgets
import sys
import pygame
from BalloonConstants import * # does it matter where we import these. Obviously, yes. We don't want to be overwriting them some places. Then again, since they are constants, they can probably be imported everywhere.
from BalloonMgr import *

# 2 - Define Constants
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BACKGROUND_COLOR = (0, 180, 180)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 640
PANEL_HEIGHT = 60
USABLE_WINDOW_HEIGHT = WINDOW_HEIGHT - PANEL_HEIGHT
FRAMES_PER_SECOND = 30

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Load assets: image(s), soudn(s), etc
oScoreDisplay = pygwidgets.DisplayText(window, (10, USABLE_WINDOW_HEIGHT + PANEL_HEIGHT*.4),
                                'Score: 0', textColor=BLACK,
                                backgroundColor=None, width=140, fontSize=24)
oStatusDisplay = pygwidgets.DisplayText(window, (180, USABLE_WINDOW_HEIGHT+PANEL_HEIGHT*.4), '',
                                        textColor=BLACK, backgroundColor=None, 
                                        width=300, fontSize=24)
oStartButton = pygwidgets.TextButton(window, 
                        (WINDOW_WIDTH - 110, USABLE_WINDOW_HEIGHT + 10), 'Start')

# 5 - Initialize variables
oBalloonMgr = BalloonMgr(window, WINDOW_WIDTH, USABLE_WINDOW_HEIGHT)
playing = False

#6 - Enter Game Loop
while True:
    #7 - Event-Driven Program
    nPointsEarned = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #
        if playing:
            oBalloonMgr.handleEvent(event) #what's the event while playing?
            theScore = oBalloonMgr.getScore() #update score after event
            oScoreDisplay.setValue('Score: ' + str(theScore)) #display score
        elif oStartButton.handleEvent(event): #so, if any event occurs while not playing, 
            oBalloonMgr.start() #start the balloon manager (so, event must be a start)
            oScoreDisplay.setValue('Score: 0') #set score to 0
            playing = True #start playing
            oStartButton.disable() 
    # do any "per frame" actions
    if playing:
        oBalloonMgr.update()
        nPopped = oBalloonMgr.getCountPopped()
        nMissed = oBalloonMgr.getCountMissed()
        oStatusDisplay.setValue('Popped: ' + str(nPopped) + '  Missed: ' + str(nMissed) + 
                                '  Out of: ' + str(N_BALLOONS) )
        # natural end-of-game condition
        if (nPopped + nMissed) == N_BALLOONS: 
            playing = False
            oStartButton.enable()
    # 9 - Clear the window
    window.fill(BACKGROUND_COLOR)
    # 10 - draw all window elements
    if playing:
        oBalloonMgr.draw()
    pygame.draw.rect(window, GRAY, pygame.Rect(0, USABLE_WINDOW_HEIGHT, WINDOW_WIDTH, PANEL_HEIGHT))
    oScoreDisplay.draw()
    oStatusDisplay.draw()
    oStartButton.draw()
    # 11 - Update the window
    pygame.display.update()
    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)


