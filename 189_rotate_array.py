from typing import List


class Solution:
    def rotate3(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        while i < k:
            digit = nums.pop()
            nums.insert(0, digit)
            i += 1
        print(nums)


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    Solution().rotate3(nums=nums, k=k)
