import pygame
from pygame.locals import *
import sys
import pygwidgets
import time

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 240
WHITE = (255, 255, 255)
FRAMES_PER_SECOND = 30
TIMER_LENGTH = 2.5

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

headerMessage = pygwidgets.DisplayText(window, (0,50), f'Click start to start a {TIMER_LENGTH} second timer:', fontSize=36, justified='center', width=WINDOW_WIDTH)
startButton = pygwidgets.TextButton(window, (200, 100), 'Start')
clickMeButton = pygwidgets.TextButton(window, (320, 100), 'Click Me')
timerMessage = pygwidgets.DisplayText(window, (0, 160), 'Mesage showing during timer', fontSize=36, justified='center', width=WINDOW_WIDTH)

timerMessage.hide()
timerRunning=False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #
        if startButton.handleEvent(event):
            timeStarted = time.time()
            startButton.disable()
            timerMessage.show()
            print('Starting timer')
            timerRunning=True
        #
        if clickMeButton.handleEvent(event):
            print('Other button was clicked')
    # Do any per frame actions - each while loop each of these are checked
    if timerRunning:
        elapsed = time.time() - timeStarted
        if elapsed >= TIMER_LENGTH:
            startButton.enable()
            timerMessage.hide()
            print('Timer ended by elapsed time')
            timerRunning = False
    #
    window.fill(WHITE)
    #
    headerMessage.draw()
    startButton.draw()
    clickMeButton.draw()
    timerMessage.draw()
    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)
