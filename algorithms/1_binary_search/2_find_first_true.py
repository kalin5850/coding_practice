"""
Find the First True in a Sorted Boolean Array

An array of boolean values is divided into two sections; the left section consists of all false and the right section consists of all true. Find the First True in a Sorted Boolean Array of the right section, i.e. the index of the first true element. If there is no true element, return -1.

Input: arr = [false, false, true, true, true]

Output: 2

Explanation: first true's index is 2.
"""

from typing import List


# TODO
def find_boundary_recursive(arr: List[bool]) -> int:
    left, right = 0, len(arr) - 1

    def recursive(arr: List[bool], left: int, right: int) -> int:
        first_true_index = -1
        middle = (left + right) // 2
        if arr[middle]:
            return middle

        return first_true_index

    return


def find_boundary(arr: List[bool]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    left, right = 0, len(arr) - 1
    first_true_index = -1

    while left <= right:

        middle = (left + right) // 2

        if arr[middle]:
            right = middle - 1
            first_true_index = middle
        else:
            left = middle + 1

    return first_true_index


if __name__ == "__main__":
    arr1 = [False, False, True, True, True]
    arr2 = [True]
    arr3 = [False, False, False]
    arr3 = [False, False, False, False, False, False, False, False, True]
    res = find_boundary(arr3)
    print(res)
