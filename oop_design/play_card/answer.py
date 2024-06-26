from enum import Enum
from typing import List


class Card:
    @property
    def card_value(self) -> int:
        raise NotImplementedError()

    def __lt__(self, other):
        return self.card_value < other.card_value


class Suit(Enum):
    CLUBS = "clubs"
    DIAMONDS = "diamonds"
    HEARTS = "hearts"
    SPADES = "spades"


class PlayingCard(Card):
    SUITS = {
        "Clubs": Suit.CLUBS,
        "Diamonds": Suit.DIAMONDS,
        "Hearts": Suit.HEARTS,
        "Spades": Suit.SPADES,
    }
    SUIT_NAME = {e: n for n, e in SUITS.items()}
    VALUES = {
        "A": 1,
        **{str(i): i for i in range(2, 11)},
        "J": 11,
        "Q": 12,
        "K": 13,
    }
    VALUE_NAME = {e: n for n, e in VALUES.items()}

    def __init__(self, suit: str, value: str) -> None:
        super().__init__()
        self.__suit = self.SUITS[suit]
        self.__value = self.VALUES[value]

    @property
    def card_value(self) -> int:
        return self.__value

    def __str__(self) -> str:
        suit = self.SUIT_NAME[self.__suit]
        value = self.VALUE_NAME[self.__value]

        return "%s of %s" % (value, suit)


class Game:
    def __init__(self):
        # Implement initializer here
        self.__cards: List[Card] = []

    def add_card(self, suit: str, value: str) -> None:
        # Implement function here
        self.__cards.append(PlayingCard(suit, value))

    def card_string(self, card: int) -> str:
        # Implement function here
        return str(self.__cards[card])

    def card_beats(self, card_a: int, card_b: int) -> bool:
        # Implement function here
        return self.__cards[card_a] > self.__cards[card_b]


if __name__ == "__main__":
    game = Game()
    # suit, value = input().split()
    suit, value = "Spades", "3"
    game.add_card(suit, value)
    print(game.card_string(0))
    # suit, value = input().split()
    suit, value = "Hearts", "K"
    game.add_card(suit, value)
    print(game.card_string(1))
    print("true" if game.card_beats(0, 1) else "false")
