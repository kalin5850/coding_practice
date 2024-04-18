import heapq


def get_minimum_window(original: str, check: str) -> str:
    # WRITE YOUR BRILLIANT CODE HERE
    if len(original) == 0 or len(check) == 0:
        return ""

    counter, window = {}, {}
    for ch in check:
        counter[ch] = 1 + counter.get(ch, 0)

    l = 0
    result, result_len = [], len(original) + 1
    have, need = 0, len(counter)
    for r in range(len(original)):
        ch = original[r]
        window[ch] = 1 + window.get(ch, 0)
        if ch in counter and counter[ch] == window[ch]:
            have += 1

        while have == need:
            # update resule
            if (r - l + 1) <= result_len:
                result_len = r - l + 1
                heapq.heappush(result, (result_len, original[l : r + 1]))
            window[original[l]] -= 1
            if original[l] in counter and window[original[l]] < counter[original[l]]:
                have -= 1
            l += 1
    return heapq.heappop(result)[1] if result else ""


if __name__ == "__main__":
    original = "cdbaebaecd"
    check = "abc"
    res = get_minimum_window(original, check)
    print(res)
