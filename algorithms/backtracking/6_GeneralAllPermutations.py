"""
Given a string of unique letters, find all of its distinct permutations.

Permutation means arranging things with an order. For example, permutations of [1, 2] are [1, 2] and [2, 1]. Permutations are best visualized with trees.
"""

from typing import List


def permutations(letters: str) -> List[str]:
    result = []

    def backtracking(idx: int, path: List[str], ckecked: List[str]):
        if len(path) == len(letters):
            result.append("".join(path))
            return

        for idx, letter in enumerate(letters):
            if letter in ckecked:
                continue
            path.append(letter)
            ckecked.append(letter)
            backtracking(idx + 1, path, ckecked)
            path.pop()
            ckecked.pop()

        return

    backtracking(0, [], [])

    return result


if __name__ == "__main__":
    # letters = input()
    letters = "abc"
    res = permutations(letters)
    for line in sorted(res):
        print(line)
