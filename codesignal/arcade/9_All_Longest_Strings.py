"""
Given an array of strings, return another array containing all of its longest strings.

Example

For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
solution(inputArray) = ["aba", "vcd", "aba"].

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.string inputArray

A non-empty array.

Guaranteed constraints:
1 ≤ inputArray.length ≤ 10,
1 ≤ inputArray[i].length ≤ 10.

[output] array.string

Array of the longest strings, stored in the same order as in the inputArray.
"""


def solution(inputArray):
    """
    Brute force: O(n * m)
    BCR: O(n)
    """
    max_length = max(len(word) for word in inputArray)
    result = [word for word in inputArray if len(word) == max_length]
    return result
