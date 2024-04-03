def fibonacci_resursion(index):
    # O(n)
    cache = {}

    def fast_fibonacci(n):
        if n in cache:
            return cache[n]
        else:
            if n < 2:
                cache[n] = n
                return cache[n]
            else:
                cache[n] = fast_fibonacci(n - 1) + fast_fibonacci(n - 2)
                return cache[n]

    fast_fibonacci(index)

    return cache[index]


if __name__ == "__main__":
    print(fibonacci_resursion(10))
