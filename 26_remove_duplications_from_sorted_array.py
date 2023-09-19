from typing import List


class Solution:
    def remove_duplicates1(self, nums: List[int]) -> int:
        "set data structure"
        data = set()
        for num in nums:
            data.add(num)

        return len(data)

    def remove_duplicates2(self, nums: List[int]) -> int:
        "hashmap"
        data = dict()
        for num in nums:
            if num not in data:
                data[num] = 1

        return len(data)

    def remove_duplicates3(self, nums: List[int]) -> int:
        "use array"
        index_1 = 0
        index_2 = 1
        while True:
            if index_2 == len(nums):
                break
            if nums[index_1] == nums[index_2]:
                index_2 += 1
            else:
                nums[index_1 + 1] = nums[index_2]
                index_2 += 1
                index_1 += 1

        return index_1 + 1

    def remove_duplicates4(self, nums: List[int]) -> int:
        "use array"
        j = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[j]:
                nums[j + 1] = nums[i]
                j += 1

        return j + 1


if __name__ == "__main__":
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

    # print(Solution().remove_duplicates1(nums=nums))
    # print(Solution().remove_duplicates2(nums=nums))
    print(Solution().remove_duplicates3(nums=nums))
