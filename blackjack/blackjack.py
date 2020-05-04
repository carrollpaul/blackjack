import random
import sys
import pygame as pg
from helpers import Deck, Card, Player, Settings
from helpers import printGreeting, getBet, analyzeHand, playHand

pg.init()

def main():
    # Initialize pygame screen
    settings = Settings()
    screen = pg.display.set_mode((
        settings.screen_width, settings.screen_height))
    table_image = pg.image.load("blackjack/images/blackjack-table.png")
    table_rect = table_image.get_rect()
    screen_rect = screen.get_rect()

    screen.blit(table_image, table_rect)

    # Set game caption
    #pg.display.set_caption(printGreeting())

    # Initialize clock timer
    clock = pg.time.Clock()

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.exit()
                sys.exit()
        
        pg.display.flip()
        
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