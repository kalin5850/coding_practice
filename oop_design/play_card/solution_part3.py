"""
Spade > Heart > Diamond > Club
"""

from enum import Enum
from typing import List


class CardBase:
    @property
    def value(self) -> int:
        raise NotImplementedError()

    def __gt__(self, other) -> bool:
        return self.value > other.value


class Suit(Enum):
    SPADES = "Spades"
    HEARTS = "Hearts"
    DIAMONDS = "Diamonds"
    CLUBS = "Clubs"


class Card(CardBase):
    SUITS = {
        "Hearts": Suit.HEARTS,
        "Spades": Suit.SPADES,
        "Clubs": Suit.CLUBS,
        "Diamonds": Suit.DIAMONDS,
    }
    VALUES = {"A": 1, **{str(i): i for i in range(2, 11)}, "J": 11, "Q": 12, "K": 13}
    VALUE_KEYS = {value: key for key, value in VALUES.items()}

    def __init__(self, suit: str, value: str) -> None:
        super().__init__()
        self.__suit = self.SUITS[suit]
        self.__value = self.VALUES[value]

    @property
    def value(self) -> int:
        return self.__value

    def __str__(self) -> str:
        return "%s of %s" % (self.VALUE_KEYS[self.__value], self.__suit.value)


class JokerColor(Enum):
    RED = "Red"
    BLACK = "Black"


class Joker(CardBase):
    COLORS = {"Red": JokerColor.RED, "Black": JokerColor.BLACK}
    VALUES = {"Black": 14, "Red": 15}

    def __init__(self, color: str) -> None:
        self.__color = color
        self.__value = self.VALUES[color]

    @property
    def value(self) -> int:
        return self.__value

    def __str__(self) -> str:
        return "%s Joker" % (self.COLORS[self.__color].value)


class Hand:
    __cards: List[Card] = []

    def __init__(self, cards: List[Card] = None) -> None:
        self.__cards = [*cards]

    def __str__(self) -> str:
        return ", ".join(str(card) for card in self.cards)

    def __lt__(self, other) -> bool:
        for card_a, card_b in zip(
            reversed(sorted(self.cards)), reversed(sorted(other.cards))
        ):
            if card_a > card_b:
                return True
        return False

    @property
    def cards(self):
        return self.__cards


class Game:
    def __init__(self):
        self.__cards: List[Card] = []
        self.__hands: List[Hand] = []

    def add_card(self, suit: str, value: str) -> None:
        card = Card(suit, value)
        self.__cards.append(card)

    def card_string(self, card: int) -> str:
        return self.__cards[card]

    def card_beats(self, card_a: int, card_b: int) -> bool:
        return self.__cards[card_a] > self.__cards[card_b]

    def add_joker(self, color: str) -> None:
        self.__cards.append(Joker(color))

    def add_hand(self, card_indices: List[int]) -> None:
        self.__hands.append(Hand(self.__cards[i] for i in card_indices))

    def hand_string(self, hand: int) -> str:
        return self.__hands[hand]

    def hand_beats(self, hand_a: int, hand_b: int) -> bool:
        return self.__hands[hand_a] > self.__hands[hand_b]


if __name__ == "__main__":
    game = Game()

    hand_a_list = []
    n_1 = [("Spades", "K"), ("Clubs", "6"), ("Diamonds", "Q")]
    for idx, card in enumerate(n_1):
        suit, value = card
        game.add_joker(value) if suit == "Joker" else game.add_card(suit, value)
        hand_a_list.append(idx)
    game.add_hand(hand_a_list)
    print(game.hand_string(0))

    hand_b_list = [] = []
    n_2 = [("Hearts", "K"), ("Diamonds", "9"), ("Spades", "7")]
    for idx, card in enumerate(n_2):
        suit, value = card
        game.add_joker(value) if suit == "Joker" else game.add_card(suit, value)
        hand_b_list.append(idx + len(n_1))
    game.add_hand(hand_b_list)
    print(game.hand_string(1))
    print("true" if game.hand_beats(0, 1) else "false")
