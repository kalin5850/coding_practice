from typing import List


def move_zeros(nums: List[int]) -> None:
    idx_i = 0  # check 0
    idx_j = 0  # check non-zero

    while idx_i < len(nums) and idx_j < len(nums):
        while nums[idx_i] != 0:
            idx_i += 1
        idx_j = idx_i  # start finding non-zero next to idx_i
        while idx_j < len(nums) and nums[idx_j] == 0:
            idx_j += 1

        if idx_i < len(nums) and idx_j < len(nums):
            nums[idx_i], nums[idx_j] = nums[idx_j], nums[idx_i]
            idx_i += 1
            idx_j += 1

    return nums


if __name__ == "__main__":
    # nums = [int(x) for x in input().split()]
    nums = [1, 0, 2, 0, 0, 7]
    move_zeros(nums)
    print(" ".join(map(str, nums)))
    nums = [3, 1, 0, 1, 3, 8, 9]
    move_zeros(nums)
    print(" ".join(map(str, nums)))
    nums = [0, 0, 9, 4, 0, 0, 3, 8, 0]
    move_zeros(nums)
    print(" ".join(map(str, nums)))
