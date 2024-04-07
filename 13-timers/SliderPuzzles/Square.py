# Square Class

import pygame
from Constants import *
from Tile import *

class Square():
    '''
    A Square is a square area of the game board, in the application window.
    Each square has a location, rectangle, a tuple of legal moves, and a
    Tile that is drawn on the Square.  For each user move, the game tells
    the clicked on Square to exchange its Tile with the blank (empty space) Square.
    '''
    def __init__(self, window, left, top, squareNumber, legalMovesTuple):
        self.window = window
        self.rect = pygame.Rect(left,top, SQUARE_WIDTH, SQUARE_HEIGHT) #pygame object which can detect mouse click events, etc.
        self.squareNumber = squareNumber
        self.legalMovesTuple = legalMovesTuple
        self.loc = (left, top)
        self.reset()
    #
    def reset(self):
        self.oTile = Tile(self.window, self.squareNumber)
    #
    def isTileInProperPlace(self) -> bool:
        tileNumber = self.oTile.getTileNumber()
        return (self.squareNumber == tileNumber)
    #
    def getLegalMoves(self) -> tuple:
        return self.legalMovesTuple
    #
    def clickedInside(self, mouseLoc) -> bool:
        hit = self.rect.collidepoint(mouseLoc)
        return hit 
    #
    def getSquareNumber(self) -> int:
        return self.squareNumber
    #
    def switch(self, oOtherSquare):
        self.oTile, oOtherSquare.oTile = oOtherSquare.oTile, self.oTile
    #
    def draw(self):
        self.oTile.draw(self.loc)


# for testing
if __name__ == "__main__":
    WINDOW_WIDTH = 470
    WINDOW_HEIGHT = 560
    FRAMES_PER_SECOND = 30
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    oSquare = Square(window,0, 0, 0, (1,2,3))