from typing import List


def word_break(s: str, words: List[str]) -> bool:
    cached = {}

    def backtracking(idx):
        if idx == len(s):
            return True

        if idx in cached:
            return cached[idx]

        ans = False
        for i, prefix in enumerate(words):
            if s[idx : idx + len(prefix)] == prefix:
                if backtracking(idx + len(prefix)):
                    ans = True
                cached[idx] = ans

        return ans

    return backtracking(0)


if __name__ == "__main__":
    # s = input()
    s = "aab"
    # words = input().split()
    words = ["a", "aa", "b"]
    res = word_break(s, words)
    print("true" if res else "false")
