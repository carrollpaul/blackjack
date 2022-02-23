import random
import typing


class Card:
    def __init__(self, rank: typing.Any, suit: str) -> None:
        self.rank = rank
        self.suit = suit

    def __repr__(self) -> str:
        return f"({self.rank}, {self.suit})"


class Deck:
    def __init__(self, shuffle_cards=False):
        self.cards = []
        self.shuffle_cards = shuffle_cards
        self.build()

    def build(self) -> None:  # Make a 52 card deck
        for rank in [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]:
            for suit in ["S", "H", "D", "C"]:
                self.cards.append(Card(rank, suit))
        if self.shuffle_cards:
            self.shuffle(self.cards)

    def shuffle(self) -> None:  # Shuffle deck
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def dealCard(self) -> Card:  # Deal one card from deck
        return self.cards.pop()


class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.hand = []
        self.bank = 100

    def __repr__(self) -> str:
        return self.name

    def getHand(self, deck: Deck, size: int) -> None:  # Deal hand equal to given size
        for i in range(size):
            self.hand.append(deck.dealCard())


def printGreeting() -> None:
    print("\n*************************\n\nWelcome to Paul's Casino!\n\n*************************\n")


def getBet(player: Player) -> int:  # Get bet from player
    while True:
        try:  # Make sure bet is a number
            bet = int(input("Input bet: "))
        except:
            print("Enter numeric bet please.")
            continue
        if player.bank - bet > 0:  # Player can't bet more than they have
            return bet
        else:
            print(f"You can't bet what you don't have! Your bankroll is ${player.bank}.")
            continue


def analyzeHand(hand: list[Card]) -> int:  # Get value of hand
    score = 0
    ace = False
    for card in hand:
        rank = card.rank
        if rank == "A":
            score += 1
            ace = True
        elif rank == "K" or rank == "Q" or rank == "J":
            score += 10
        else:
            score += int(rank)
    if not ace:
        return score
    elif (
        score < 11
    ):  # If a hand containing one or more aces valued at 1 is less than 11, change value of one ace to 11 (add 10)
        score += 10
        return score
    else:
        return score


def playHand(
    player: Player, dealer: Player, deck: Deck
) -> None:  # Function for a single hand of blackjack
    print(f"Your bank: {player.bank}")
    bet = getBet(player)

    dealer.getHand(deck, 2)  # Deal 2 cards to player and dealer
    player.getHand(deck, 2)

    print(f"{player.name}'s hand: {player.hand}")  # Print player's hand and 1 card of dealer's hand
    print(f"{dealer.name}'s hand: {dealer.hand[0]}")

    # Check for blackjack
    playerScore = analyzeHand(player.hand)
    if playerScore == 21:
        print("Blackjack!")
        player.bank = player.bank + bet * 1.5
        return

    # Loop for player
    while True:
        while True:
            hit = input("Hit? (y/n): ")  # See if player wants to hit or stand
            # Make sure input is y or n
            if hit.upper() == "Y" or hit.upper() == "N":
                break
            else:
                print("Please enter 'y' or 'n'.")
                continue

        if hit.upper() == "N":
            playerScore = analyzeHand(player.hand)
            break
        else:
            player.getHand(deck, 1)  # If hit, deal one card and print new hand, then analyze hand
            print(f"{player.name}'s hand: {player.hand}")
            playerScore = analyzeHand(player.hand)
            if playerScore > 21:
                print("Bust!")
                player.bank = player.bank - bet
                return
            if playerScore == 21:
                break
            else:
                continue

    # Loop for dealer
    while True:
        print(f"{dealer.name}'s hand: {dealer.hand}")

        dealerScore = analyzeHand(dealer.hand)

        if dealerScore > 21:
            print("Dealer busts, you win!")
            player.bank += bet
            return
        elif dealerScore > playerScore:
            print("Better luck next time!")
            player.bank -= bet
            return
        elif dealerScore >= 17:  # Dealer will hit if below player's hand and below 17
            if dealerScore == playerScore:
                print("Push!")
                return
            if dealerScore < playerScore:
                print("You win!")
                player.bank += bet
                return
            else:
                print("Better luck next time!")
                player.bank -= bet
                return
        else:
            dealer.getHand(deck, 1)
