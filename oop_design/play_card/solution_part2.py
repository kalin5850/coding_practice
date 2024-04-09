from enum import Enum


class CardBase:
    @property
    def value(self) -> int:
        raise NotImplementedError()

    def __lt__(self, other) -> bool:
        return self.value < other.value


class Suit(Enum):
    HEARTS = "Hearts"
    SPADES = "Spades"
    CLUBS = "Clubs"
    DIAMONDS = "Diamonds"


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
        return "%s of Joker" % (self.COLORS[self.__color].value)


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

    def add_joker(self, color: str) -> None:
        self.__list.append(Joker(color))


if __name__ == "__main__":
    game = Game()
    suit, value = "Spades", "3"
    game.add_card(suit, value)
    print(game.card_string(0))
    suit, value = "Hearts", "K"
    game.add_card(suit, value)
    print(game.card_string(1))
    print("true" if game.card_beats(0, 1) else "false")
    suit, value = "Joker", "Red"
    game.add_joker(value)
    print(game.card_string(2))
    suit, value = "Joker", "Black"
    game.add_joker(value)
    print(game.card_string(3))
    print("true" if game.card_beats(2, 3) else "false")
    print("true" if game.card_beats(0, 3) else "false")
