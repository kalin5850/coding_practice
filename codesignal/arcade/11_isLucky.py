"""
Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.

Given a ticket number n, determine if it's lucky or not.

Example

For n = 1230, the output should be
solution(n) = true;
For n = 239017, the output should be
solution(n) = false.
Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] integer n

A ticket number represented as a positive integer with an even number of digits.

Guaranteed constraints:
10 ≤ n < 106.

[output] boolean

true if n is a lucky ticket number, false otherwise.
"""


def solution(n):
    """
    time complexity: O(n)
    space complexity: O(1)
    """
    number_string = str(n)
    left, right = 0, len(number_string) - 1
    left_sum, right_sum = 0, 0

    while left < right:
        left_sum += int(number_string[left])
        right_sum += int(number_string[right])
        left += 1
        right -= 1

    return left_sum == right_sum
