"""
Note: Try to solve this task in-place (with O(1) additional memory), since this is what you'll be asked to do during an interview.

You are given an n x n 2D matrix that represents an image. Rotate the image by 90 degrees (clockwise).

Example

For

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
the output should be

solution(a) =
    [[7, 4, 1],
     [8, 5, 2],
     [9, 6, 3]]
"""


def solution(a):
    """
    brute force: O(n ^ 2)
    BCR: O(n)
    """
    result = list()
    for i in range(len(a)):
        tmp = []
        for j in range(len(a) - 1, -1, -1):
            tmp.append(a[j][i])
        result.append(tmp)

    return result
