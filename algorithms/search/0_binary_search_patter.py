from typing import List


def binary_search(arr: List[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    first_true_idx = -1

    while left <= right:
        # middle = left + math.Floor((right - left) // 2)
        middle = (left + right) // 2
        if feasible(middle):
            first_true_idx = middle
            right = middle - 1
        else:
            left = middle + 1

    return first_true_idx
