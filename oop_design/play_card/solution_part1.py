from enum import Enum, auto


class Suit(Enum):
    HEARTS = "Hearts"
    SPADES = "Spades"
    CLUBS = "Clubs"
    DIAMONDS = "Diamonds"


class Card:
    SUITS = {
        "Hearts": Suit.HEARTS,
        "Spades": Suit.SPADES,
        "Clubs": Suit.CLUBS,
        "Diamonds": Suit.DIAMONDS,
    }
    VALUES = {"A": 1, **{str(i): i for i in range(2, 11)}, "J": 11, "Q": 12, "K": 13}
    VALUE_KEYS = {value: key for key, value in VALUES.items()}

    def __init__(self, suit: str, value: str) -> None:
        self.__suit = self.SUITS[suit]
        self.__value = self.VALUES[value]

    def __str__(self) -> str:
        return "%s of %s" % (self.VALUE_KEYS[self.__value], self.__suit.value)

    def __lt__(self, other):
        return self.__value > other.__value


class Game:
    def __init__(self):
        self.__list = []

    def add_card(self, suit: str, value: str) -> None:
        card = Card(suit, value)
        self.__list.append(card)

    def card_string(self, card: int) -> str:
        return self.__list[card]

    def card_beats(self, card_a: int, card_b: int) -> bool:
        return self.__list[card_a] > self.__list[card_b]


if __name__ == "__main__":
    game = Game()
    suit, value = "Spades", "3"
    game.add_card(suit, value)
    print(game.card_string(0))
    suit, value = "Hearts", "K"
    game.add_card(suit, value)
    print(game.card_string(1))
    print("true" if game.card_beats(0, 1) else "false")
