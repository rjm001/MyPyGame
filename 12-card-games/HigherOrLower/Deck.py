# Deck class

import random
from Card import *

class Deck():
    SUIT_TUPLE = {'Diamonds', 'Clubs','Hearts','Spades'}
    STANDARD_DICT = {'Ace':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':11,'Queen':12, 'King':13 }
    #
    def __init__(self, window, rankValueDict=STANDARD_DICT):
        self.startingDeckList = []
        self.playingDeckList = []
        for suit in Deck.SUIT_TUPLE:
            for rank, value in rankValueDict.items():
                oCard = Card(window, rank, suit, value)
                self.startingDeckList.append(oCard)
        #
        self.shuffle()
    #
    def shuffle(self):
        # Copy the starting deck and save it in the playing deck list so don't have to track as pop off of the playingDeck
        self.playingDeckList = self.startingDeckList.copy()
        for oCard in self.playingDeckList:
            oCard.conceal()
        random.shuffle(self.playingDeckList) #so, random has a function that does all the work!
    #
    def getCard(self):
        if len(self.playingDeckList) == 0:
            raise IndexError('No more cards')
        #popping off the back of the deck
        oCard = self.playingDeckList.pop()
        return oCard
    #
    def returnCardToDeck(self, oCard):
        #put a card at front of deck (end)
        self.playingDeckList.insert(0, oCard)

# for testing

if __name__ == '__main__':
    # if run this file directly, runs this MVP to test if Deck class works
    import pygame
    WINDOW_WIDTH=100
    WINDOW_HEIGHT=100
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    oDeck = Deck(window)
    for i in range(1, 53):
        oCard = oDeck.getCard()
        print('Name: ', oCard.getName(), ' Value:', oCard.getValue())