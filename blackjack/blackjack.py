import random
from helpers import Card, Deck, Player
from helpers import printGreeting, getBet, analyzeHand, playHand


def main() -> None:
    printGreeting()

    deck = Deck()  # Make and shuffle deck
    deck.shuffle()

    playerName = input("What's your name? ")  # Get name of player

    player = Player(playerName)  # Create player and dealer objects
    dealer = Player("Dealer")

    playHand(player, dealer, deck)  # Play first hand

    while True:  # Start main game loop
        if len(deck.cards) < 10:  # If deck has less than 10 cards, make a new deck
            deck = Deck()
        if player.bank < 1:  # Make sure player has money
            print("You're broke! Come back with more money.")
            break

        print(f"Your bank: {player.bank}")

        while True:
            playAgain = input("Play again? (y/n): ")  # Check if player wants to play another hand
            if playAgain.upper() == "Y" or playAgain.upper() == "N":  # Make sure input is y or n
                break
            else:
                print("Please enter 'y' or 'n'.")
                continue

        if playAgain == "n":
            print("Thanks for playing! Come again soon")
            break
        else:
            player.hand.clear()  # "Discard" player and dealer hands
            dealer.hand.clear()
            playHand(player, dealer, deck)


if __name__ == "__main__":
    main()
