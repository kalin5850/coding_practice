"""
Given a sorted array of integers and a target integer, find the first occurrence of the target and return its index. Return -1 if the target is not in the array.

Input:

arr = [1, 3, 3, 3, 3, 6, 10, 10, 10, 100]
target = 3
Output: 1

Explanation: The first occurrence of 3 is at index 1.

Input:

arr = [2, 3, 5, 7, 11, 13, 17, 19]
target = 6
Output: -1
"""

from typing import List


def find_first_occurrence(arr: List[int], target: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    left, right = 0, len(arr) - 1
    first_true_idx = -1

    while left <= right:

        middle = (left + right) // 2

        if arr[middle] == target:
            first_true_idx = middle
            right = middle - 1
        elif arr[middle] > target:
            right = middle - 1
        else:
            left = middle + 1

    return first_true_idx
