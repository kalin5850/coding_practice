# Playing Cards

For this question, we ask you to design a card game using the traditional 52-card deck. We divide this question in to three parts, so you can complete them in order.

## Part One

For the first part, you must design a Game class representing the game, and these following functions associated with the class.

1. add_card(suit, value): Creates a new card object with a suit from one of the following strings: Hearts, Spades, Clubs, Diamonds, and a value from one of the following strings: A, 2~10, J, Q, K. This card is represented by i, where i is an integer indicating how many cards have been created before.
2. card_string(card): Returns the string representation of the card represented by i. It follows the format <value> of <suit>. For example, a card created by add_card("Spades", "3") should have a string representation of 3 of Spades.
3. card_beats(card_a, card_b): Check if the card represented by card_a beats the one represented by card_b. A card beats another card if and only if it has a greater value. The value of the cards are ordered from A to K.

You may implement these however you like. However, preferably this should be easily expandable to accommodate new requirements.

```python
class Game:
    def __init__(self):
        # Implement initializer here
        pass

    def add_card(self, suit: str, value: str) -> None:
        # Implement function here
        pass

    def card_string(self, card: int) -> str:
        # Implement function here
        return ""

    def card_beats(self, card_a: int, card_b: int) -> bool:
        # Implement function here
        return False

if __name__ == '__main__':
    game = Game()
    suit, value = input().split()
    game.add_card(suit, value)
    print(game.card_string(0))
    suit, value = input().split()
    game.add_card(suit, value)
    print(game.card_string(1))
    print("true" if game.card_beats(0, 1) else "false")

```

## Part Two

For this part, we ask you to implement the Jokers into the system.

In addition to the functionalities above, also implement the following functions:

1. add_joker(color): Creates a Joker card of with color of either Red or Black.

   - Joker beats everything else except other jokers. This card is represented by i, where i is an integer indicating how many cards have been created before, including both normal cards and jokers.

   - A joker's string representation is Red Joker or Black Joker, depending on the color.
     You may copy the code from the previous question here.

```python
class Game:
    def __init__(self):
        # Implement initializer here
        pass

    def add_card(self, suit: str, value: str) -> None:
        # Implement function here
        pass

    def card_string(self, card: int) -> str:
        # Implement function here
        return ""

    def card_beats(self, card_a: int, card_b: int) -> bool:
        # Implement function here
        return False

    def add_joker(self, color: str) -> None:
        # Implement function here
        pass
```

## Part Three

This game also involve a concept of a Hand and comparing the size of the two hands. For this part, add these following functions to the Game class:

add_hand(card_indices): Create a new Hand with cards represented by the list of integer representation of cards card_indices. The hand can be represented by i, where i is the number of hands added before.
hand_string(hand): Return the string representation of the hand represented by hand. It is a list of string representation of cards by their insertion order, separated by ", ". For example, if hand has a 9 of Clubs, K of Hearts, and a Black Joker, the string representation is "9 of Clubs, K of Hearts, Black Joker".
beats_hand(hand_a, hand_b): Check if the hand represented by hand_a beats the hand represented by hand_b according to the following rules:
Starting from the largest card in each hand, compare them. If a card beats another, that hand beats the other hand. Otherwise, compare the next largest card.
Repeat this process until one hand beats the other, or one hand runs out of cards. If a hand runs out of cards, neither hand beat each other.

```python
from typing import List

class Game:
    def __init__(self):
        # Implement initializer here
        pass

    def add_card(self, suit: str, value: str) -> None:
        # Implement function here
        pass

    def card_string(self, card: int) -> str:
        # Implement function here
        return ""

    def card_beats(self, card_a: int, card_b: int) -> bool:
        # Implement function here
        return False

    def add_joker(self, color: str) -> None:
        # Implement function here
        pass

    def add_hand(self, card_indices: List[int]) -> None:
        # Implement function here
        pass

    def hand_string(self, hand: int) -> str:
        # Implement function here
        return ""

    def hand_beats(self, hand_a: int, hand_b: int) -> bool:
        # Implement function here
        return False
```
