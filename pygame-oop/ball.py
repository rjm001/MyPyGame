import pygame
from pygame.locals import *
import random

class Ball():
    
    def __init__(self, window, windowWidth, windowHeight) -> None:
        self.window = window #storing the window so we can draw on it later
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.image = pygame.image.load("images/ball.png")
        ballRect = self.image.get_rect()
        self.width = ballRect.width
        self.height = ballRect.height
        self.maxWidth = windowWidth - self.width
        self.maxHeight = windowHeight - self.height

        # random starting position
        self.x = random.randrange(0, self.maxWidth)
        self.y = random.randrange(0, self.maxHeight)

        # Choose a random speed between -4 and 4, but not zero
        # in both the x and y directions
        speedsList = [-4, -3, -2, -1, 1, 2, 3, 4]
        self.xSpeed = random.choice(speedsList)
        self.ySpeed = random.choice(speedsList)
    
    # note we just have one update method, to update speed and position from new speed
    # Technically the speed's are distances gained rather than speeds. But they induce speed.
    def update(self):
        # check for hitting a wall. if so, change the direction
        if (self.x < 0) or (self.x >= self.maxWidth):
            self.xSpeed = -self.xSpeed
        
        if (self.y < 0) or (self.y >= self.maxHeight):
            self.ySpeed = -self.ySpeed
        
        # update the Ball's x and y, using the speed in both directions
        self.x = self.x + self.xSpeed
        self.y = self.y + self.ySpeed

    def draw(self):
        self.window.blit(self.image, (self.x, self.y))
    
    # added this method to reset the ball's position and speed
    def reset(self):
        # random starting position
        self.x = random.randrange(0, self.maxWidth)
        self.y = random.randrange(0, self.maxHeight)

        # Choose a random speed between -4 and 4, but not zero,
        # in both the x and y directions
        speedsList = [-4, -3, -2, -1, 1, 2, 3, 4]
        self.xSpeed = random.choice(speedsList)
        self.ySpeed = random.choice(speedsList)
    