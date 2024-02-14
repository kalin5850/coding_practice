"""
Given an array Arr[] of size N, print all the subsets of the array.

Subset: A subset of an array is a tuple that can be obtained from the array by removing some (possibly all) elements of it

Example:
Input: N = 3, Arr = [1, 2, 3]
Output: 
{}
{1}
{1, 2}
{1, 2, 3}
{1, 3}
{2}
{2, 3}
{3}
"""
from typing import List


def calcSubset(A: List, res: List, subset: List[int], index: int) -> List:
    # Add the current subset to the result list
    res.append(subset.copy())

    # Generate subsets by recursively including and excluding elements
    for i in range(index, len(A)):
        # Include the current element in the subset
        subset.append(A[i])

        # Recursively generate subsets with the current element included
        calcSubset(A, res, subset, i + 1)

        # Exclude the current element from the subset (backtracking)
        subset.pop()

    return res


# Driver code
if __name__ == "__main__":
    array = [1, 2, 3]
    res = calcSubset(array, [], [], 0)

    # Print the generated subsets
    for subset in res:
        print(*subset)
