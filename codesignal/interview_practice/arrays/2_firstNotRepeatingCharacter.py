"""
Given a string s consisting of small English letters, find and return the first instance of a non-repeating character in it. If there is no such character, return '_'.

Example

For s = "abacabad", the output should be
solution(s) = 'c'.

There are 2 non-repeating characters in the string: 'c' and 'd'. Return c since it appears in the string first.

For s = "abacabaabacaba", the output should be
solution(s) = '_'.

There are no characters in this string that do not repeat.
"""


def solution(s):
    """
    brute force: O(n ^ 2)
    BCR: O(n)
    """
    a_dict = {}
    for ch in s:
        if ch not in a_dict:
            a_dict[ch] = 1
        else:
            a_dict[ch] = a_dict[ch] + 1

    for ch, value in a_dict.items():
        if value == 1:
            return ch

    return "_"
