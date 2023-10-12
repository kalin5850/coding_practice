import itertools
from typing import List


class Solution:
    def permutation1(self, strings: str) -> List[str]:
        char_list = list(strings)
        permutations = list(itertools.permutations(char_list))

        return ["".join(permutation) for permutation in permutations]

    def permutation2(self, ch: List[str], curr_idx=0) -> List[str]:
        """Time complexity is O(n * n!) and space complexity is O(1)"""

        def swap(ch, i, j):
            temp = ch[i]
            ch[i] = ch[j]
            ch[j] = temp

        if curr_idx == len(ch) - 1:
            print("".join(ch))

        for i in range(curr_idx, len(ch)):
            swap(ch, curr_idx, i)
            self.permutation2(ch, curr_idx + 1)
            swap(ch, curr_idx, i)  # backtracking

    def permutation3(self, remaining, candidate=""):
        if len(remaining) == 0:
            print(candidate)
        for i in range(len(remaining)):
            new_candidate = candidate + remaining[i]
            new_remaning = remaining[0:i] + remaining[i + 1 :]
            self.permutation3(new_remaning, new_candidate)


if __name__ == "__main__":
    string = "abc"
    # print(Solution().permutation1(strings=string))
    # print(Solution().permutation2(ch=list(string)))
    # print(Solution().permutation3(remaining=list(string)))

    string = [1, 2, 3]
    print(Solution().permutation3(remaining=string))
