from typing import List


class Solution:
    def search1(self, nums: List[int], target: int) -> int:
        if len(nums) == 1 and nums[0] == target:
            return 0
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (right + left) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1

        return -1

    def search2(self, nums: List[int], target: int) -> int:
        return nums.index(target) if target in nums else -1


if __name__ == "__main__":
    import heapq

    item = [20, 4, 8, 10, 5, 7, 6, 2, 9]
    heapq.heapify(item)  # transforms list into a heap, in-place, in linear time

    print("Heap obtained from heapify() : ", item)
    print("The popped and smallest element is : ", end="")
    print(heapq.heappop(item))
    from _heapq import _heappop_max, _heapify_max, _heapreplace_max

    a = [20, 4, 8, 10, 5, 7, 6, 2, 9]
    _heapify_max(a)

    print("Heap obtained from _heappop_max() : ", a)
    print("The popped and max element is : ", end="")
    print(heapq.heappop(a))
