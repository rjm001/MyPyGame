# Game Class. An OMO of an OMO!

import pygwidgets
from Constants import *
from Deck import *
from Card import *

# Idea, what if the game shows you all the cards for three seconds then lets you play?
# could just call showcard on all of them then hide again
# perhaps even could hide in a random order
# perhaps even could move them in view after hiding like a gambler's game
class Game():
    CARD_OFFSET = 110
    CARDS_TOP = 300
    CARDS_LEFT = 75
    NCARDS = 8
    POINTS_CORRECT = 15
    POINTS_INCORRECT = 10
    #
    def __init__(self, window):
        self.window = window
        self.oDeck = Deck(self.window)
        self.score = 100
        self.scoreText = pygwidgets.DisplayText(window, (450, 164), 'Score: ' + str(self.score), fontSize=36, textCoolor=WHITE, justified='right')
        self.messageText = pygwidgets.DisplayText(window, (50, 460), '', width=900, justified='center', fontSize=36, textColor=WHITE)
        self.loserSound = pygame.mixer.Sound('sounds/loser.wav')
        self.winnerSound = pygame.mixer.Sound('sounds/ding.wave')
        self.cardShuffleSound = pygame.mixer.Sound('sounds/cardShuffle.wave')
        self.cardXPositionsList = []
        thisLeft = Game.CARDS_LEFT #accessing class variable!
        # Calculate the x positions of all cards, once
        for cardNum in range(Game.NCARDS):
            self.cardXPositionsList.append(thisLeft)
            thisLeft = thisLeft + Game.CARD_OFFSET
        #
        self.reset()
    # Method for a new round
    def reset(self):
        pass
    #
    def getCardNameAndValue(self, index):
        pass
    #
    def showCard(self, index):
        oCard = self.cardList[index]
        oCard.reveal()
    #
    def hitHigherOrLower(self, higherOrLower):
        pass
    #
    def draw(self):
        for oCard in self.cardList:
            oCard.draw()
        #
        self.scoreText.draw()
        self.messageText.draw()


