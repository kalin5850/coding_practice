import collections
import heapq
from typing import List


class Solution:
    def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
        # use bucket sort if the answer is not unique.
        if len(nums) == 1:
            return nums
        nums_times = collections.Counter(nums)
        bucket = [[] for i in range(len(nums))]
        result = []
        for num, times in nums_times.items():
            bucket[times - 1].append(num)
        bucket = list(filter(None, bucket))
        print(bucket)
        if len(bucket) < k:
            return bucket.pop()
        for i in range(k):
            result.extend(bucket.pop())

        return result

    def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
        nums_counter = collections.Counter(nums)
        nums_counter = [(-freq, num) for num, freq in nums_counter.items()]
        # max heap
        heapq.heapify(nums_counter)
        results = []
        for _ in range(k):
            item = heapq.heappop(nums_counter)
            results.append(item[1])

        return results
