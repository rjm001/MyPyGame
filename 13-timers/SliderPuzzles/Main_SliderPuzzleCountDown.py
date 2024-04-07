# Slider Puzzle Game with Count Down Timer
import pygame
from pygame.locals import *
from Constants import *
import pygwidgets
import pyghelpers
import sys
from Game import *

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
restartButton = pygwidgets.CustomButton(window, (320, 455),
                                        up='images/restartButtonUp.jpg',
                                        down='images/restartButtonDown.jpg',
                                        over='images/restartButtonOver.jpg')
clock = pygame.time.Clock()
timerDisplay = pygwidgets.DisplayText(window, (50, 465), '',
                                    fontSize=36, textColor=WHITE)
messageDisplay = pygwidgets.DisplayText(window, (50, 510), 'Click on a tile to move it.',
                                    fontSize=36, textColor=WHITE)
oGame = Game(window)  # create the main game object
soundBuzz = pygame.mixer.Sound('sounds/buzz.wav')
oCountDownTimer = pyghelpers.CountDownTimer(180)  # create a count down clock timer
oCountDownTimer.start()  # start the clock running

while True:
    for event in pygame.event.get():
        # check if the event is the X button
        if event.type == pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            messageDisplay.setText('')
            oGame.gotClick(event.pos)
            over = oGame.checkForWin()
            if over:
                messageDisplay.setText('Great job!!!')
                oCountDownTimer.stop()

        if restartButton.handleEvent(event):
            #print('Got click on restart button')
            oGame.startNewGame()
            oCountDownTimer.start()
    timeToShow = oCountDownTimer.getTimeInHHMMSS(2)
    timerDisplay.setValue(f'Time: {timeToShow}')
    if oGame.getGamePlaying():
        if oCountDownTimer.ended():
            soundBuzz.play()
            messageDisplay.setValue('Doh! You ran out of time!')
            oGame.stopPlaying()
        
    window.fill(BLACK)
    oGame.draw()
    restartButton.draw()
    timerDisplay.draw()
    messageDisplay.draw()
    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)