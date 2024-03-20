"""
We have a message consisting of digits 0-9 to decode. Letters are encoded to digits by their positions in the alphabet

1A -> 1
2B -> 2
3C -> 3
4...
5Y -> 25
6Z -> 26
Given a non-empty string of digits, how many ways are there to decode it?

Input: "18"

Output: 2

Explanation: "18" can be decoded as "AH" or "R"

Input: "123"

Output: 3

Explanation: "123" can be decoded as "ABC", "LC", "AW"
"""


def decode_ways(digits: str) -> int:
    def backtracking(idx):
        if idx == len(digits):
            return 1

        if digits[idx] == "0":
            return 0

        ways = 0
        # decode one digit
        ways = ways + backtracking(idx + 1)
        # decode two digits
        if 9 < int(digits[idx : idx + 2]) <= 26:
            ways = ways + backtracking(idx + 2)

        return ways

    return backtracking(0)


# cached
def decode_ways(digits: str) -> int:

    def backtracking(idx, cached):
        if idx in cached:
            return cached[idx]

        if idx == len(digits):
            return 1

        if digits[idx] == "0":
            return 0

        ways = 0
        # decode one digit
        ways = ways + backtracking(idx + 1)
        # decode two digits
        if 9 < int(digits[idx : idx + 2]) <= 26:
            ways = ways + backtracking(idx + 2)

        cached[idx] = ways
        return ways

    return backtracking(0, {})


if __name__ == "__main__":
    # digits = input()
    digits = "123"
    res = decode_ways(digits)
    print(res)
