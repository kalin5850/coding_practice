"""
Given a sorted list of numbers, remove duplicates and return the new length. You must do this in-place and without using extra memory.

Input: [0, 0, 1, 1, 1, 2, 2].

Output: 3.

Your function should modify the list in place so the first 3 elements becomes 0, 1, 2. Return 3 because the new length is 3.
"""

from typing import List


def remove_duplicates(arr: List[int]) -> int:
    slow, fast = 0, 0
    while fast < len(arr):
        if arr[slow] == arr[fast]:
            fast += 1
        else:
            slow += 1
            arr[slow] = arr[fast]

    return slow + 1


if __name__ == "__main__":
    # arr = [int(x) for x in input().split()]
    arr = [0, 0, 1, 1, 1, 2, 2]
    res = remove_duplicates(arr)
    print(" ".join(map(str, arr[:res])))
    arr = [1, 2, 3]
    res = remove_duplicates(arr)
    print(" ".join(map(str, arr[:res])))
    arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    res = remove_duplicates(arr)
    print(" ".join(map(str, arr[:res])))
