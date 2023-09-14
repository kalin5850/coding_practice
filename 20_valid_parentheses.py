class Solution:
    def is_valid1(self, s: str) -> bool:
        length = len(s)
        for i in range(length):
            for j in range(length):
                if s[i] == "(" and s[j] == ")":
                    break
                elif s[i] == ")" and s[j] == "(":
                    break
                elif s[i] == "[" and s[j] == "]":
                    break
                elif s[i] == "]" and s[j] == "[":
                    break
                elif s[i] == "{" and s[j] == "}":
                    break
                elif s[i] == "}" and s[j] == "{":
                    break
                else:
                    return False

        return True


if __name__ == "__main__":
    input = "()[]"
    print(Solution().is_valid1(s=input))
