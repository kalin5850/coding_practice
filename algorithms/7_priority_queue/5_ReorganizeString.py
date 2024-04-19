"""
Given a string s, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result. If not possible, return the empty string.

Example 1:

Input:s = "aab"

Output: aba

Example 2:

Input:s = "aaab"

Output: ``

Note:

s will consist of lowercase letters and have length in the range [1, 500].
"""

import heapq
from collections import Counter
from typing import Counter


def reorganize_string(s: str) -> str:
    # WRITE YOUR BRILLIANT CODE HERE
    frequency = Counter(s)
    max_heap = [[-value, key] for key, value in frequency.items()]
    heapq.heapify(max_heap)
    result = ""
    on_hold = None

    while len(max_heap):
        count, ch = heapq.heappop(max_heap)  # start most frequency
        result += ch
        count += 1
        if on_hold:
            heapq.heappush(max_heap, on_hold)
            on_hold = None
        if count != 0:
            on_hold = [count, ch]

    return result if len(result) == len(s) else ""


if __name__ == "__main__":
    s = "aab"
    # s = "aaab"
    # s = "bbaa"
    # s = "banana"
    # s = "lllllooooooooolllll"
    # s = "aaaeaiaoau"
    res = reorganize_string(s)
    if not res:
        print("Impossible")
        exit()
    input_counter, output_counter = Counter(s), Counter(res)
    if input_counter != output_counter:
        print("Not rearrangement")
        exit()
    for i in range(len(res) - 1):
        if res[i] == res[i + 1]:
            print(f"Same character at index {i} and {i+1}")
            exit()
    print("Valid")
