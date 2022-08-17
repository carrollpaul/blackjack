import random
import typing
from dataclasses import dataclass


@dataclass
class Card:
    rank: typing.Any
    suit: str

    def __repr__(self) -> str:
        return f"({self.rank}, {self.suit})"


class Deck:
    def __init__(self, shuffle_cards: bool = False) -> None:
        self.cards = []
        self.build(shuffle_cards)

    def build(self, shuffle_cards: bool = False) -> None:
        """Make a 52 card deck."""
        for rank in [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]:
            for suit in ["S", "H", "D", "C"]:
                self.cards.append(Card(rank, suit))
        if shuffle_cards:
            self.shuffle(self.cards)

    def shuffle(self) -> None:
        """Shuffle deck."""
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def deal_card(self) -> Card:
        """Deal one card from deck"""
        return self.cards.pop()


class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.hand = []
        self.bank = 100

    def __repr__(self) -> str:
        return self.name

    def get_hand(self, deck: Deck, size: int) -> None:
        """Deal hand equal to given size."""
        for _ in range(size):
            self.hand.append(deck.deal_card())


def get_bet(player: Player) -> int:  # Get bet from player
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


def analyze_hand(hand: list[Card]) -> int:
    """Determine highest possible value of hand."""
    score = 0
    ace = False
    for card in hand:
        rank = card.rank
        if rank == "A":
            score += 1
            ace = True
        elif rank in ["K", "Q", "J"]:
            score += 10
        else:
            score += int(rank)

    if not ace:
        return score

    # If a hand containing one or more aces valued at 1 is less than 11,
    # change value of one ace to 11 (add 10)
    elif score < 11:
        score += 10
        return score

    else:
        return score


def play_hand(player: Player, dealer: Player, deck: Deck) -> None:
    """Play a single hand of blackjack."""

    print(f"Your bank: {player.bank}")
    bet = get_bet(player)

    # Deal 2 cards to player and dealer
    dealer.get_hand(deck, 2)
    player.get_hand(deck, 2)

    # Print player's hand and 1 card of dealer's hand
    print(f"{player.name}'s hand: {player.hand}")
    print(f"{dealer.name}'s hand: {dealer.hand[0]}")

    # Check for blackjack
    player_score = analyze_hand(player.hand)
    if player_score == 21:
        print("Blackjack!")
        player.bank = player.bank + bet * 1.5
        return

    # Loop for player
    while True:
        while True:
            hit = input("Hit? (y/n): ").lower()
            if hit in ["y", "n"]:
                break

            print("Please enter 'y' or 'n'.")

        if hit == "n":
            player_score = analyze_hand(player.hand)
            break

        # If hit, deal one card and print new hand, then analyze hand
        player.get_hand(deck, 1)
        print(f"{player.name}'s hand: {player.hand}")
        player_score = analyze_hand(player.hand)
        if player_score > 21:
            print("Bust!")
            player.bank = player.bank - bet
            return
        if player_score == 21:
            break

    # Loop for dealer
    while True:
        print(f"{dealer.name}'s hand: {dealer.hand}")

        dealer_score = analyze_hand(dealer.hand)

        if dealer_score > 21:
            print("Dealer busts, you win!")
            player.bank += bet
            return
        elif dealer_score > player_score:
            print("Better luck next time!")
            player.bank -= bet
            return

        # Dealer will hit if below player's score and below 17
        elif dealer_score >= 17:
            if dealer_score == player_score:
                print("Push!")
                return
            if dealer_score < player_score:
                print("You win!")
                player.bank += bet
                return

            print("Better luck next time!")
            player.bank -= bet
            return

        dealer.get_hand(deck, 1)
