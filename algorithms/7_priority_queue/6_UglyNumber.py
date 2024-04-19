def nth_ugly_number(n: int) -> int:
    i = 0
    nums = [1]
    prime_factor = [2, 3, 5]

    while i < n:
        tmp = []
        tmp = list(map(lambda x: nums[i] * x, prime_factor))
        nums += tmp
        nums = list(set(nums))
        nums.sort()
        i += 1

    return nums[n - 1]


if __name__ == "__main__":
    n = 25
    res = nth_ugly_number(n)
    print(res)
