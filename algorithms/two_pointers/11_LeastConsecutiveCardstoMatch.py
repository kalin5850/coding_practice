"""
Given a list of integers cards, your goal is to match a pair of cards, but you can only pick up cards in a consecutive manner. What's the minimum number of cards that you need to pick up to make a pair? If there are no matching pairs, return -1.

For example, given cards = [3, 4, 2, 3, 4, 7], then picking up [3, 4, 2, 3] makes a pair of 3s and picking up [4, 2, 3, 4] matches two 4s. We need 4 consecutive cards to match a pair of 3s and 4 consecutive cards to match 4s, so you need to pick up at least 4 cards to make a match.
"""

from typing import List


def least_consecutive_cards_to_match(cards: List[int]) -> int:
    result = []
    for slow in range(len(cards) - 1):
        fast = slow + 1
        while fast <= len(cards) - 1:
            if cards[fast] not in cards[slow:fast]:
                fast += 1
            else:
                result.append(len(cards[slow:fast]) + 1)
                break
    return min(result) if len(result) else -1
