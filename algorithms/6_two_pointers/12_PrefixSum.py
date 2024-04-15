def prefix_sum_array(arr):
    prefix_sum = [0]
    for num in arr:
        prefix_sum.append(prefix_sum[-1] + num)
    return prefix_sum


arr = [1, -20, -3, 30, 5, 4]
print(prefix_sum_array(arr))
# [0, 1, -19, -22, 8, 13, 17]

from typing import List


def subarray_sum(arr: List[int], target: int) -> List[int]:
    # brute force
    for i in range(len(arr) - 1):
        tmp = arr[i]
        for j in range(i + 1, len(arr)):
            tmp += arr[j]
            if tmp == target:
                return [i, j + 1]


def subarray_sum(arr: List[int], target: int) -> List[int]:
    # prefix sum
    prefix_sum = {0: 0}
    cur_sum = 0
    for i in range(len(arr)):
        cur_sum += arr[i]
        complement = cur_sum - target
        if complement in prefix_sum:
            return [prefix_sum[complement], i + 1]
        prefix_sum[cur_sum] = i + 1


if __name__ == "__main__":
    arr = [1, 3, -3, 8, 5, 7]
    target = 5
    res = subarray_sum(arr, target)
    print(" ".join(map(str, res)))
    arr = [1, 1, 1]
    target = 3
    res = subarray_sum(arr, target)
    print(" ".join(map(str, res)))
    arr = [1, -20, -3, 30, 5, 7]
    target = 7
    res = subarray_sum(arr, target)
    print(" ".join(map(str, res)))
