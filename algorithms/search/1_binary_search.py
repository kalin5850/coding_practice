from typing import List


def binary_search(arr: List[int], target: int) -> int:
    left, right = 0, len(arr) - 1

    while left <= right:
        # or left + math.Floor((right - left) // 2) with other language
        middle = (right + left) // 2

        if arr[middle] == target:
            return middle
        if arr[middle] > target:
            right = middle - 1
        else:
            left = middle + 1
    return -1


def binary_search_recursive(
    target: int, sorted_array: List[int], left: int, right: int
) -> int:
    if right < left:
        return -1

    middle = (left + right) // 2

    if sorted_array[middle] == target:
        return middle
    elif sorted_array[middle] < target:
        return binary_search_recursive(target, sorted_array, middle + 1, right)
    else:
        return binary_search_recursive(target, sorted_array, left, middle - 1)


if __name__ == "__main__":
    nums = [1, 2, 4, 5, 6, 44, 63, 87, 99, 283]
    print(binary_search(nums, 99))
    print(binary_search_recursive(99, nums, 0, len(nums) - 1))
