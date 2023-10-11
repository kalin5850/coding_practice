from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            middle = (low + high) // 2
            if nums[middle] == target:
                return middle
            if nums[middle] > target:
                high = middle - 1
            if nums[middle] < target:
                low = middle + 1
        if nums[middle] > target:
            return middle
        return middle + 1


if __name__ == "__main__":
    input = [1, 3, 5, 6]
    target = 5
    print(Solution().searchInsert(input, target))
