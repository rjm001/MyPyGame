# Tile Class

import pygame
from Constants import *

class Tile():
    """
    A Tile contains a tile number and an associated image
    """
    font = pygame.font.SysFont(None, 60)
    def __init__(self, window, tileNumber):
        self.window = window
        self.tileNumber = tileNumber
        # Use drawing calls to create a surface for each tile
        #   For the empty tile, just a filled tile
        #   For all others, draw a circle, and center a number in it
        #
        # Alternatively, we could load image tiles from a folder:
        # self.image = pygame.image.load('images/tile' + str(self.tileNumber + 1) + '.png')
        surface = pygame.Surface((SQUARE_WIDTH, SQUARE_HEIGHT))
        if self.tileNumber == STARTING_OPEN_SQUARE_NUMBER:
            surface.fill(GRAY)
            pygame.draw.rect(surface, BLACK, pygame.Rect((0,0,SQUARE_WIDTH, SQUARE_HEIGHT)), 2)
        else:
            surface.fill(PURPLE)
            pygame.draw.rect(surface, BLACK, pygame.Rect((0,0, SQUARE_WIDTH, SQUARE_HEIGHT)),2)
            centerX = SQUARE_WIDTH // 2
            centerY = SQUARE_HEIGHT // 2
            pygame.draw.circle(surface, YELLOW, (centerX, centerY), 35)
            numberAsImage = Tile.font.render(str(self.tileNumber + 1), True, BLACK)
            widthOfNumber = numberAsImage.get_width()
            leftPos = (SQUARE_WIDTH - widthOfNumber) // 2 
            heightOfNumber = numberAsImage.get_height()
            topPos = (SQUARE_HEIGHT - heightOfNumber) // 2 
            surface.blit(numberAsImage, (leftPos, topPos))
        #
        self.image = surface
    #
    def getTileNumber(self):
        return self.tileNumber
    #
    def draw(self, loc):
        self.window.blit(self.image, loc)


# for testing purposes
if __name__ == "__main__":
    WINDOW_WIDTH = 470
    WINDOW_HEIGHT = 560
    FRAMES_PER_SECOND = 30
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    oSquare = Tile(window,0)
