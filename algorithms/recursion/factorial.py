def factorial_resursion(n):
    if n > 0:
        return n * factorial_loop(n - 1)


def factorial_loop(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    print(factorial_resursion(5))
    print(factorial_loop(5))
