import pygame
import random
from pygame.locals import *
import pygwidgets
from BalloonConstants import *
from abc import ABC, abstractmethod #used to create abstract base classes

#abstract base class
class Balloon(ABC):
    popSoundLoaded = False #class variable
    popSound= None # load when first balloon is created; class variable
    #
    @abstractmethod #note, no colon `:` after decorators
    def __init__(self, window, maxWidth, maxHeight, ID, oImage, size, nPoints, speedY):
        self.window = window
        self.ID = ID
        self.balloonImage = oImage #why these names no match? convention when should and shouldn't?
        self.size = size
        self.nPoints = nPoints
        self.speedY = speedY
        if not Balloon.popSoundLoaded: #load first time only
            Balloon.popSoundLoaded=True #so not loaded next. (this is a class variable!)
            Balloon.popSound = pygame.mixer.Sound('sounds/balloonPop.wav')
        #
        balloonRect = self.balloonImage.getRect()
        self.width = balloonRect.width
        self.height = balloonRect.height
        self.x = random.randrange(maxWidth - self.width)
        self.y = maxHeight + random.randrange(75)
        self.balloonImage.setLoc((self.x, self.y))
    #
    def clickedInside(self, mousePoint):
        myRect = pygame.Rect(self.x, self.y, self.width, self.height)
        if myRect.collidepoint(mousePoint):
            Balloon.popSound.play()
            return True, self.nPoints #true means was hit. note, returning two things!
        else:
            return False, 0 #not hit, no points
    #
    def update(self):
        self.y = self.y - self.speedY
        self.balloonImage.setLoc((self.x, self.y))
        if self.y < -self.height: #if it escapes
            return BALLOON_MISSED
        else:
            return BALLOON_MOVING
    #
    def draw(self): #just a wrapper method really
        self.balloonImage.draw()
    #
    def __del__(self):
        print(self.size, 'Balloon', self.ID, 'is going away')



class BalloonSmall(Balloon):
    balloonImage = pygame.image.load('images/redBalloonSmall.png') 
    def __init__(self, window, maxWidth, maxHeight, ID):
        oImage = pygwidgets.Image(window, (0,0), BalloonSmall.balloonImage)
        super().__init__(window, maxWidth, maxHeight, ID, oImage, 'Small', 30, 3.1)


class BalloonMedium(Balloon):
    balloonImage = pygame.image.load('images/redBalloonMedium.png') 
    def __init__(self, window, maxWidth, maxHeight, ID):
        oImage = pygwidgets.Image(window, (0,0), BalloonMedium.balloonImage)
        super().__init__(window, maxWidth, maxHeight, ID, oImage, 'Medium', 20, 2.2)


class BalloonLarge(Balloon):
    balloonImage = pygame.image.load('images/redBalloonLarge.png') 
    def __init__(self, window, maxWidth, maxHeight, ID):
        oImage = pygwidgets.Image(window, (0,0), BalloonLarge.balloonImage)
        super().__init__(window, maxWidth, maxHeight, ID, oImage, 'Large', 10, 1.5)


class MegaBalloon(Balloon):
    balloonImage = pygame.image.load('images/megaBalloon.png') 
    def __init__(self, window, maxWidth, maxHeight, ID):
        oImage = pygwidgets.Image(window, (0,0), MegaBalloon.balloonImage)
        self.clickCount = 0
        super().__init__(window, maxWidth, maxHeight, ID, oImage, 'Mega', 50, 1.3)
    #
    def clickedInside(self, mousePoint):
        myRect = pygame.Rect(self.x, self.y, self.width, self.height)
        if myRect.collidepoint(mousePoint):            
            if self.clickCount < 3:
                self.clickCount += 1
                return True, 0
            else:
                Balloon.popSound.play()
                return True, self.nPoints
        else:
            return False, 0
        




