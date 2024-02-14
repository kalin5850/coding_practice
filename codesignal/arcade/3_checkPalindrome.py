"""
Given the string, check if it is a palindrome.

Example

For inputString = "aabaa", the output should be
solution(inputString) = true;
For inputString = "abac", the output should be
solution(inputString) = false;
For inputString = "a", the output should be
solution(inputString) = true.
"""


def solution(inputString):
    """
    brute force: O(n ^ 2)
    BCR: O(n)
    """
    if len(inputString) == 1:
        return True

    right_idx = len(inputString) - 1
    for left_idx, ch in enumerate(inputString):
        # print("%s == %s, %s == %s" % (inputString[left_idx], inputString[right_idx], left_idx, right_idx))
        if left_idx == right_idx:
            return True
        if inputString[left_idx] == inputString[right_idx]:
            right_idx -= 1
        else:
            return False

    return True
