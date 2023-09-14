class Solution:
    def is_valid1(self, s: str) -> bool:
        count_open_par = 0
        count_close_par = 0
        count_open_sq = 0
        count_close_sq = 0
        count_open_cur = 0
        count_close_cur = 0

        for ch in s:
            if ch == "(":
                count_open_par += 1
            elif ch == ")":
                count_close_par += 1
            elif ch == "[":
                count_open_sq += 1
            elif ch == "]":
                count_close_sq += 1
            elif ch == "{":
                count_open_cur += 1
            elif ch == "}":
                count_close_cur += 1

        return (
            count_open_par == count_close_par
            and count_open_sq == count_close_sq
            and count_open_cur == count_close_cur
        )


if __name__ == "__main__":
    input = "()["
    print(Solution().is_valid1(s=input))
