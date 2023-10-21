class Solution:
    def urlify(self, input: str) -> str:
        result = ""
        for idx, ch in enumerate(input[0]):
            if ch != " ":
                result += ch
            elif ch == " " and idx < input[1] - 1:
                result += "%20"

        return result


if __name__ == "__main__":
    input = ("Mr John Smith    ", 13)
    print(Solution().urlify(input))
