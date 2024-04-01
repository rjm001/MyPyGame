# BalloonMgr class
import pygame
import random
from pygame.locals import *
import pygwidgets
#from BalloonConstants import *
from Balloon import *

class BalloonMgr():
    def __init__(self, window, maxWidth, maxHeight) -> None:
        self.window = window
        self.maxWidth = maxWidth
        self.maxHeight = maxHeight
    #
    def start(self):
        self.balloonList = []
        self.nPopped = 0
        self.nMissed = 0 
        self.score = 0
        #
        for balloonNum in range(0, N_BALLOONS):
            randomBalloonClass = random.choice((BalloonSmall, BalloonMedium, BalloonLarge, MegaBalloon))
            #randomBalloonClass = random.choice((BalloonSmall, BalloonMedium, BalloonLarge))
            oBalloon = randomBalloonClass(self.window, self.maxWidth, self.maxHeight, balloonNum) #balloonNum is ID
            self.balloonList.append(oBalloon)
        #
    def handleEvent(self, event):
        if event.type == MOUSEBUTTONDOWN:
            # Go 'reversed' so toppmost baloon gets popped
            for oBalloon in reversed(self.balloonList):
                wasHit, nPoints = oBalloon.clickedInside(event.pos)
                if wasHit:
                    if nPoints > 0:
                        self.balloonList.remove(oBalloon)
                        self.nPopped = self.nPopped + 1
                        self.score = self.score + nPoints
                    return
    #
    def update(self):
        for oBalloon in self.balloonList:
            status = oBalloon.update()
            if status == BALLOON_MISSED:
                # Ballooo went off 
                self.balloonList.remove(oBalloon)
                self.nMissed += 1
    #
    def getScore(self):
        return self.score
    #
    def getCountPopped(self):
        return self.nPopped
    #
    def getCountMissed(self):
        return self.nMissed
    #
    def draw(self):
        for oBalloon in self.balloonList:
            oBalloon.draw()

    