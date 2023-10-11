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

    def is_valid2(self, s: str) -> bool:
        "use stack data structure"
        if len(s) < 2:
            return False
        parentheses_stack = []
        for ch in s:
            if ch == "(" or ch == "[" or ch == "{":
                parentheses_stack.append(ch)
            else:
                if (
                    not parentheses_stack
                    or ch == ")"
                    and parentheses_stack[-1] != "("
                    or ch == "]"
                    and parentheses_stack[-1] != "["
                    or ch == "}"
                    and parentheses_stack[-1] != "{"
                ):
                    return False
                parentheses_stack.pop()
        return not parentheses_stack


if __name__ == "__main__":
    input = "(])"
    print(Solution().is_valid2(s=input))
