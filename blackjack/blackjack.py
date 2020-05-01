import random
import sys
import pygame as pg
from helpers import Deck, Card, Player, Settings

pg.init()

def printGreeting():
    print("\n*************************\n\nWelcome to Paul's Casino!\n\n*************************\n")

def getBet(player): # Get bet from player
    while True: 
        try: # Make sure bet is a number
            bet = int(input('Input bet: '))
        except:
            print('Enter numeric bet please.')
            continue
        if (player.bank - bet > 0): # Player can't bet more than they have
            return bet
        else: 
            print(f"You can't bet what you don't have! Your bankroll is ${player.bank}.")
            continue

def analyzeHand(hand): # Get value of hand
    score = 0
    ace = False
    for card in hand:
        rank = card.rank
        if (rank == 'A'):
            score += 1
            ace = True
        elif (rank == 'K' or rank == 'Q' or rank == 'J'):
            score += 10
        else:
            score += int(rank)
    if not ace:
        return score
    elif score < 11: # If a hand containing one or more aces valued at 1 is less than 11, change value of one ace to 11 (add 10)
        score += 10
        return score 
    else:
        return score

def playHand(player, dealer, deck): # Function for a single hand of blackjack
    bet = getBet(player)

    dealer.getHand(deck, 2) # Deal 2 cards to player and dealer
    player.getHand(deck, 2)

    print(f"{player.name}'s hand: {player.hand}") # Print player's hand and 1 card of dealer's hand
    print(f"{dealer.name}'s hand: {dealer.hand[0]}")

    # Check for blackjack
    playerScore = analyzeHand(player.hand)
    if (playerScore == 21):
        print('Blackjack!')
        player.bank = player.bank + bet*1.5
        return
    
    # Loop for player
    while True:
        while True:
            hit = input('Hit? (y/n): ') # See if player wants to hit or stand
            # Make sure input is y or n
            if hit.upper() == 'Y' or hit.upper() == 'N': 
                break
            else:
                print("Please enter 'y' or 'n'.")
                continue

        if (hit.upper() == 'N'):
            playerScore = analyzeHand(player.hand)
            break
        else:
            player.getHand(deck, 1) # If hit, deal one card and print new hand, then analyze hand
            print(f"{player.name}'s hand: {player.hand}")
            playerScore = analyzeHand(player.hand)
            if (playerScore > 21):
                print('Bust!')
                player.bank = player.bank - bet
                return
            if (playerScore == 21):
                break
            else:
                continue

    # Loop for dealer           
    while True:       
        print(f"{dealer.name}'s hand: {dealer.hand}")

        dealerScore = analyzeHand(dealer.hand)

        if dealerScore > 21:
            print('Dealer busts, you win!')
            player.bank += bet
            return
        elif dealerScore > playerScore:
            print('Better luck next time!')
            player.bank -= bet
            return
        elif dealerScore >= 17: # Dealer will hit if below player's hand and below 17
            if dealerScore == playerScore:
                print('Push!')
                return
            if dealerScore < playerScore:
                print('You win!')
                player.bank += bet
                return
            else:
                print('Better luck next time!')
                player.bank -= bet
                return
        else:
            dealer.getHand(deck, 1)

def main():
    # Initialize pygame screen
    settings = Settings()
    screen = pg.display.set_mode((
        settings.screen_width, settings.screen_height))

    # Set game caption
    pg.display.set_caption(printGreeting())

    # Initialize clock timer
    clock = pg.time.Clock()

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.exit()
                sys.exit()
        
        deck = Deck(shuffle_cards = True) # Make and shuffle deck

        playerName = input("What's your name? ") # Get name of player
        player = Player(playerName) # Create player and dealer objects
        dealer = Player('Dealer')
            
        playHand(player, dealer, deck) # Play first hand 

        while True: # Start main game loop
            if (len(deck.cards) < 10): # If deck has less than 10 cards, make a new deck
                deck = Deck()
            if player.bank < 1: # Make sure player has money
                print("You're broke! Come back with more money.")
                break

            print(f'Your bank: {player.bank}')

            while True:
                playAgain = input('Play again? (y/n): ') # Check if player wants to play another hand
                if playAgain.upper() == 'Y' or playAgain.upper() == 'N': # Make sure input is y or n
                    break
                else:
                    print("Please enter 'y' or 'n'.")
                    continue

            if playAgain == 'n':
                print('Thanks for playing! Come again soon')
                break
            else:
                player.hand.clear() # "Discard" player and dealer hands
                dealer.hand.clear()
                playHand(player, dealer, deck)

if __name__ == '__main__':
    main()