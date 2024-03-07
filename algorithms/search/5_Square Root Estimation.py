"""
Given an integer, find its square root without using the built-in square root function. Only return the integer part (truncate the decimals).

Input: 16

Output: 4

Input: 8

Output: 2

Explanation: square root of 8 is 2.83..., return the integer part, 2
"""


def square_root(n: int) -> int:
    left, right = 0, n
    result = -1
    while left <= right:
        middle = (left + right) // 2
        if middle * middle == n:
            return middle
        if middle * middle > n:
            right = middle - 1
            result = middle
        else:
            left = middle + 1

    return result - 1
