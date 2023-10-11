from typing import List


class Solution:
    ## brute force
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            remaining = target - nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j] == remaining:
                    return [i, j]

    ## hash table
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for idx, number in enumerate(nums):
            remaining = target - number
            if remaining in table:
                return [table.get(remaining), idx]
            else:
                table[number] = idx
