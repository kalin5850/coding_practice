from typing import List


class Solution:
    def containsDuplicate1(self, nums: List[int]) -> bool:
        """
        Brute force
        """
        for idx, num in enumerate(nums):
            for i in range(idx + 1, len(nums)):
                if num == nums[i]:
                    return True

        return False

    def containsDuplicate2(self, nums: List[int]) -> bool:
        """
        Hashtable
        """
        result = {}
        for num in nums:
            if num not in result:
                result[num] = 1
            else:
                return True
        return False


if __name__ == "__main__":
    input = [1, 2, 3, 4]
    print(Solution().containsDuplicate2(nums=input))
