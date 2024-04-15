def longest_substring_without_repeating_characters(s: str) -> int:
    longest_length = 0
    slow = 0
    for fast in range(1, len(s)):
        if s[fast] in s[slow:fast]:
            longest_length = max(longest_length, len(s[slow:fast]))
            while s[slow] != s[fast]:
                slow += 1
            slow += 1
        if fast == len(s) - 1:
            longest_length = max(longest_length, len(s[slow : fast + 1]))

    return longest_length


if __name__ == "__main__":
    s = "abccabcabcc"
    s = "abcdbea"
    res = longest_substring_without_repeating_characters(s)
    print(res)
