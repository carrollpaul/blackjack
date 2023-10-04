from blackjack.helpers import Deck, Player
from blackjack.helpers import play_hand


def play() -> None:
    print(
        "\n*************************\n\nWelcome to Paul's Casino!\n\n*************************\n"
    )

    deck = Deck()  # Make and shuffle deck
    deck.shuffle()

    player_name = input("What's your name? ")  # Get name of player

    player = Player(player_name)  # Create player and dealer objects
    dealer = Player("Dealer")

    play_hand(player, dealer, deck)  # Play first hand

    while True:  # Start main game loop
        if len(deck.cards) < 10:  # If deck has less than 10 cards, make a new deck
            deck = Deck()
        if player.bank < 1:  # Make sure player has money
            print("You're broke! Come back with more money.")
            break

        print(f"Your bank: {player.bank}")

        while True:
            play_again = input(
                "Play again? (y/n): "
            )  # Check if player wants to play another hand
            if (
                play_again.upper() == "Y" or play_again.upper() == "N"
            ):  # Make sure input is y or n
                break
            else:
                print("Please enter 'y' or 'n'.")

        if play_again.lower() == "n":
            print("Thanks for playing! Come again soon")
            break
        else:
            player.hand.clear()
            dealer.hand.clear()
            play_hand(player, dealer, deck)


if __name__ == "__main__":
    play()
