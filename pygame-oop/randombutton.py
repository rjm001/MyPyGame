import pygame
from pygame.locals import *
import random

class RandomButton():
    # 3 states, even though only 2 images
    STATE_IDLE = 'idle' #button up, mouse not over button
    STATE_ARMED = 'armed' #buttown down and mouse over button
    STATE_DISARMED = 'disarmed' #clicked then rolled off

    def __init__(self, window, windowwidth, windowheight, up, down) -> None:
        self.window = window
        self.windowWidth = windowwidth
        self.windowHeight = windowheight
        self.surfaceUp = pygame.image.load(up)
        self.surfaceDown = pygame.image.load(down)  

        # get the rect of the button
        self.rect = self.surfaceUp.get_rect()
        self.loc = (random.randrange(0, self.windowWidth-self.rect.width), 
                    random.randrange(0, self.windowHeight- self.rect.height))
        self.rect[0] = self.loc[0]
        self.rect[1] = self.loc[1]
        

        # set the initial state
        self.state=RandomButton.STATE_IDLE

    def handleEvent(self, event):

        #note, this returns true by Default if one of the buttons is clicked
        if self.state == RandomButton.STATE_IDLE:
            if event.type == MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
                self.state = RandomButton.STATE_ARMED
        

        elif self.state == RandomButton.STATE_ARMED:
            if event.type == MOUSEBUTTONUP and self.rect.collidepoint(event.pos):
                self.state = RandomButton.STATE_IDLE
                return True #case clicked

            elif event.type == MOUSEMOTION and not self.rect.collidepoint(event.pos):
                self.state = RandomButton.STATE_DISARMED
        
        elif self.state == RandomButton.STATE_DISARMED:
            if self.rect.collidepoint(event.pos):
                self.state = RandomButton.STATE_ARMED
            elif event.type == MOUSEBUTTONUP:
                self.state = RandomButton.STATE_IDLE

        return False

    '''
        # Copilot's suggestion to handle mouse events. Similar, just doesn't unpop if scroll off. 
        if event.type == MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.state = RandomButton.STATE_ARMED
        elif event.type == MOUSEBUTTONUP:
            if self.state == RandomButton.STATE_ARMED:
                self.state = RandomButton.STATE_DISARMED
                return True #case clicked
            else:
                self.state = RandomButton.STATE_IDLE
        return False
    '''
        
    

    def draw(self):
        # Draw the button's current appearance to the window.
        if self.state == RandomButton.STATE_ARMED:
            self.window.blit(self.surfaceDown, self.loc)
        else: #idle or disarmed
            self.window.blit(self.surfaceUp, self.loc)