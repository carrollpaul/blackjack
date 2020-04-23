import random

class Deck:
    def __init__(self):
        self.deck = []
        self.suits = ['C', 'S', 'D', 'H']
        self.ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
        for rank in ranks:
            for suit in suits:
                self.deck.append((rank, suit))

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

deck = Deck()
print(len(deck.deck))
print(deck.suits)
