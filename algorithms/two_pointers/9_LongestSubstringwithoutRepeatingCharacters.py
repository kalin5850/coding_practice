def longest_substring_without_repeating_characters(s: str) -> int:
    slow = 0
    max_length = 0
    for fast in range(1, len(s)):
        if s[fast] in s[slow:fast]:
            max_length = max(max_length, len(s[slow:fast]))
            while True:
                if s[slow] == s[fast]:
                    slow += 1
                    break
                slow += 1
        if fast == len(s) - 1:
            max_length = max(max_length, len(s[slow : fast + 1]))

    return max_length


if __name__ == "__main__":
    s = "abcdbea"
    res = longest_substring_without_repeating_characters(s)
    print(res)
