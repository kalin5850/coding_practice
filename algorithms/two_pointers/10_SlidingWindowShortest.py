from typing import List


def subarray_sum_shortest(nums: List[int], target: int) -> int:
    slow, fast = 0, 0
    min_length = len(nums) + 1

    while fast < len(nums):
        if sum(nums[slow:fast]) < target:
            fast += 1
        elif sum(nums[slow:fast]) > target:
            slow += 1
        else:
            min_length = min(min_length, len(nums[slow:fast]))
            slow += 1
            fast += 1

    return min_lengt
