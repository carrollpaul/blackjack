import random
import pygame
import os

class Settings:

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800

class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.img = pygame.image.load('C:/SourceCode/python/blackjack/images/'+str(rank)+suit+'.png')
        self.rect = self.img.get_rect()

    def __repr__(self):
        return f'({self.rank}, {self.suit})'

class Deck:

    def __init__(self, shuffle_cards = False):
        self.cards = []
        self.shuffle_cards = shuffle_cards
        self.build()

    def build(self): # Make a 52 card deck
        for rank in [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']: 
            for suit in ['S', 'H', 'D', 'C']: 
                self.cards.append(Card(rank, suit))
        if self.shuffle_cards:
            random.shuffle(self.cards)
    '''
    def shuffle(self): # Shuffle deck
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
    '''
    def dealCard(self): # Deal one card from deck
        return self.cards.pop()

class Player:

    def __init__(self, name):
        self.name = name
        self.hand = []
        self.bank = 100

    def __repr__(self):
        return self.name

    def getHand(self, deck, size): # Deal hand equal to given size
        for i in range(size):
            self.hand.append(deck.dealCard())