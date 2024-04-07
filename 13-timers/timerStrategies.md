# Timer Strategies

1. Counting Frames
2. Use pygame to create an event that is issued in the future
3. Remember a start time and continuously check for the elapsed time

- **3 is the best. It's the cleanest and most accurate approach**

## 1 Counting Frames

- See `13-timers/01CountingFrames.py`
- Everything the same as below, except:


```python
## snip
## in main while loop
for event in pygame.event.get():
    ## snip
    if startButton.handleEvent(event):
        nFramesElapsed = 0
        nFramesToWait = int(FRAMES_PER_SECOND*TIMER_LENGTH)
        startButton.disable()
        timerMessage.show()
        print('Starting timer')
        timerRunning = True
    ## snip

if timerRunning:
    nFramesElapsed = nFramesElapsed + 1
    if nFramesElapsed >= nFramesToWait:
        startButton.enable()
        timerMessage.hide()
        print('Timer ended by counting frames')
        timerRunning = False
        
## snip

```

## 2 Timer Event

- see `13-timers/02TimerEvent.py`
- Everything the same as below except

```python

## snip

TIME_EVENT_ID = pygame.event.custom_type()

## snip
while True:
    for event in pygame.event.get():
        ## snip
        if startButton.handleEvent(event):
            pygame.time.set_timer(TIMER_EVENT_ID, int(TIMER_LENGTH*1000), TRUE)
            startButton.disable() #same as 1
            timerMessage.show() # same as 1
            print('Starting timer') 
            #timerRunning = True #no longer needed
        ## snip

    ## snip

    timerMessage.draw()

    # below no longer needed
    #if timerRunning:
    #    nFramesElapsed = nFramesElapsed + 1
    #if nFramesElapsed >= nFramesToWait:
    #    startButton.enable()
    #    timerMessage.hide()
    #    print('Timer ended by counting frames')
    #    timerRunning = False

        ## snip        



```


## 3 Calculating Elapsed Time

- see `13-timers/03CalculateElapsedTime.py`

```python

import pygame
from pygame.locals import *
import sys
import pygwidgets
import time # don't need this package in first two

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 240
WHITE = (255, 255, 255)
FRAMES_PER_SECOND = 30 #takes 1/30 of a second for each frame
TIMER_LENGTH = 2.5 #2.5 seconds

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
        if evenet.type == pygame.QUIT:
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


```