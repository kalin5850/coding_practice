"""
Given input nums = [1, 6, 3, 1, 2, 4, 5] and target = 10, then the longest subarray that does not exceed 10 is [3, 1, 2, 4], so the output is 4 (length of [3, 1, 2, 4]).
"""

from typing import List


def subarray_sum_longest(nums: List[int], target: int) -> int:
    slow, max_count = 0, 0
    for fast in range(len(nums)):
        if sum(nums[slow:fast]) == target:
            max_count = len(nums[slow:fast])
            slow += 1

    return max_count
