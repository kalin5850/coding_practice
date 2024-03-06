"""
Given two strings, find the number of common characters between them.

Example

For s1 = "aabcc" and s2 = "adcaa", the output should be
solution(s1, s2) = 3.

Strings have 3 common characters - 2 "a"s and 1 "c".
"""

from collections import Counter


def solution(s1, s2):
    s1_counter = Counter(s1)
    s2_counter = Counter(s2)

    count = 0
    for key, value in s1_counter.items():
        count += min(value, s2_counter.get(key, 0))

    return count
