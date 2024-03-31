"""
Given an array of integers sorted in ascending order, find two numbers that add up to a given target. Return the indices of the two numbers in ascending order. You can assume elements in the array are unique and there is only one solution. Do this in O(n) time and with constant auxiliary space.

Input:

arr: a sorted integer array
target: the target sum we want to reach
Sample Input: [2, 3, 4, 5, 8, 11, 18], 8

Sample Output: 1 3
"""

from typing import List


def two_sum_sorted(arr: List[int], target: int) -> List[int]:
    left, right = 0, len(arr) - 1

    while True:
        if (arr[left] + arr[right]) == target:
            return [left, right]
        elif (arr[left] + arr[right]) > target:
            right -= 1
        elif (arr[left] + arr[right]) < target:
            left += 1
