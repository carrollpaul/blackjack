import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    def __repr__(self):
        return '({rank}, {suit})'.format(rank = self.rank, suit = self.suit)

class Deck:
    def __init__(self):
        self.cards = []
        self.build()
    def build(self):
        for rank in [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']:
            for suit in ['H', 'D', 'S', 'C']:
                self.cards.append((rank, suit))
    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
    def dealCard(self):
        return self.cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
    def __repr__(self):
        return self.name
    def getHand(self, deck, size):
        for i in range(size):
            self.hand.append(deck.dealCard())

def printGreeting():
    print("\n*************************\n\nWelcome to Paul's Casino!\n\n*************************\n")

def getBet():
    return input('Input bet: ')

def analyzeHand(hand):
    valueLowAce = 0
    valueHighAce = 0
    for card in hand:
        rank = card[0]
        if (rank == 'A'):
            valueLowAce = valueLowAce + 1
            valueHighAce = valueHighAce + 21
        if rank == 'K' or rank == 'Q' or rank == 'J':
            valueLowAce = valueLowAce + 10
            valueHighAce = valueHighAce +10
        else:
            valueLowAce = valueLowAce + rank
            valueHighAce = valueHighAce + rank
    return valueLowAce, valueHighAce

def playHand(player, dealer, deck, bank):
    bet = getBet()

    dealer.getHand(deck, 2)
    player.getHand(deck, 2)

    print(f"{player.name}'s hand: {player.hand}")
    print(f"{dealer.name}'s hand: {dealer.hand[0]}")

    playerScore = analyzeHand(player)
        if playerScore == 21:
            print('Blackjack!')
            bank = bank + bet*1.5
            return

def main():
    # Setup steps:
        # Print greeting
        # Make deck, shuffle it
        # Get player name
        # Make player and dealer
        # Make player bank

    # Loop game until player says stop or bank == 0

    # Steps for a given hand below:
        # Get bet from player
        # Deal player hand, deal dealer's hand
        # Show player hand
        # Show one of dealer's cards

        # Check player's hand for blackjack
            # If blackjack, return bet + bet*1.5
            # Cards are discarded
            # Hand over

        # If not blackjack, begin loop:
            # Ask to hit or stand
            # If stand, break loop
            # If hit, deal one card to player, check score of hand
                # If score is over 21:
                    # player loses bet, 
                    # break loop
                # If score = 21
                    # break loop
            # If score is less than 21
                # Continue loop

        # When player stands, dealer loop begins
            # Check score of dealer hand
            # If dealer score > 21
                # Player wins bet
                # Cards are discarded
                # Break loop
            # If dealer score > than player score
                # Player loses bet
                # Cards are discarded
                # break loop
            # If dealer score < 17
                # Deal dealer 1 card
                # Repeat loop
        
        # Hand finished

 

    printGreeting()

    deck = Deck()
    deck.shuffle()

    player = Player('Paul')
    dealer = Player('Dealer')

    bank = 100
        
    while True: # Start main game loop
        bet = getBet()
        
        dealer.getHand(deck, 2)
        player.getHand(deck, 2)

        print(f"{player.name}'s hand: {player.hand}")
        print(f"{dealer.name}'s hand: {dealer.hand[0]}")

        playerScore = analyzeHand(player)
        if playerScore == 21:
            print('Blackjack!')
            bank = bank + bet*1.5

    while True:
        score = 0
        if score > 21:
            break
        hit = input('Hit or stay (y/n): ')
        if hit == 'y':
            player.getHand(deck, 1)
            score = analyzeHand(hand)
        else:
            score = analyzeHand(hand)
            break
    
    print(f"{player.name}'s hand: {player.hand}")

if __name__ == '__main__':
    main()