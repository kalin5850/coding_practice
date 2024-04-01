"""
Given a phone number that contains digits 2-9, find all possible letter combinations the phone number could translate to.



Input:

"56"
Output:

["jm","jn","jo","km","kn","ko","lm","ln","lo"]
"""

from typing import List


def letter_combinations_of_phone_number(digits: str) -> List[str]:
    phone_dict = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
    }

    result = []

    def dfs(start_idx: int, path: List[str]):
        if start_idx == len(digits):
            result.append("".join(path))
            return

        phone_ch = digits[start_idx]
        for ch in phone_dict[phone_ch]:
            path.append(ch)
            dfs(start_idx + 1, path)
            path.pop()

        return

    dfs(0, [])

    return result


if __name__ == "__main__":
    digits = input()
    res = letter_combinations_of_phone_number(digits)
    print(" ".join(res))
