"""
Determine whether a string is a palindrome, ignoring non-alphanumeric characters and case. Examples:

Input: Do geese see God? Output: True

Input: Was it a car or a cat I saw? Output: True

Input: A brown fox jumping over Output: False
"""


def is_palindrome(s: str) -> bool:
    s = s.replace(" ", "").lower()
    left, right = 0, len(s) - 1

    while left <= right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True
