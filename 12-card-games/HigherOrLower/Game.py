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
        self.oDeck = Deck(self.window) #why call it oDeck. don't like that. whatever
        self.score = 100
        self.scoreText = pygwidgets.DisplayText(window, (450, 164), 'Score: ' + str(self.score), fontSize=36, textColor=WHITE, justified='right')
        self.messageText = pygwidgets.DisplayText(window, (50, 460), '', width=900, justified='center', fontSize=36, textColor=WHITE)
        self.loserSound = pygame.mixer.Sound('sounds/loser.wav')
        self.winnerSound = pygame.mixer.Sound('sounds/ding.wav')
        self.cardShuffleSound = pygame.mixer.Sound('sounds/cardShuffle.wav')
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
        self.cardShuffleSound.play()
        self.cardList = []
        self.oDeck.shuffle()
        for cardIndex in range(0, Game.NCARDS):
            oCard = self.oDeck.getCard()
            self.cardList.append(oCard)
            thisXPosition = self.cardXPositionsList[cardIndex]
            oCard.setLoc((thisXPosition, Game.CARDS_TOP))
        self.showCard(0)
        self.cardNumber = 0 #note don't set this at initialization time but instead reset time
        self.currentCardName, self.currentCardValue = \
            self.getCardNameAndValue(self.cardNumber)
        self.messageText.setValue('Starting card is ' + self.currentCardName + '. Will the next card be higher or lower?')
    #
    def getCardNameAndValue(self, index):
        oCard = self.cardList[index]
        theName = oCard.getName()
        theValue = oCard.getValue()
        return theName, theValue
    #
    def showCard(self, index):
        oCard = self.cardList[index]
        oCard.reveal()
    #
    def hitHigherOrLower(self, higherOrLower):
        self.cardNumber = self.cardNumber + 1
        self.showCard(self.cardNumber)
        nextCardName, nextCardValue = self.getCardNameAndValue(self.cardNumber)
        #
        if higherOrLower == HIGHER:
            if nextCardValue > self.currentCardValue:
                self.score = self.score + Game.POINTS_CORRECT
                self.messageText.setValue('Yes, the ' + nextCardName + ' was higher')
                self.winnerSound.play()
            else:
                self.score = self.score - Game.POINTS_INCORRECT
                self.messageText.setValue('No, the ' + nextCardName + ' was not higher.')
                self.loserSound.play()
        else: #user hit the lower button
            if nextCardValue < self.currentCardValue:
                self.score = self.score + Game.POINTS_CORRECT
                self.messageText.setValue('Yes, the ' + nextCardName + ' was lower')
                self.winnerSound.play()
            else:
                self.score = self.score - Game.POINTS_INCORRECT
                self.messageText.setValue('No, the ' + nextCardName + ' was not lower')
                self.loserSound.play()
        #
        self.scoreText.setValue('Score: ' + str(self.score))
        self.currentCardValue = nextCardValue
        done = (self.cardNumber == (Game.NCARDS - 1))
        return done
    #
    def draw(self):
        for oCard in self.cardList:
            oCard.draw()
        #
        self.scoreText.draw()
        self.messageText.draw()


